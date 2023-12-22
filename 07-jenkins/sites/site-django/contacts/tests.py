from django.test import TestCase, Client
from django.urls import reverse
from freezegun import freeze_time

from .models import Message


class ContactsFormTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid_form_submission(self):
        response = self.client.post(reverse('contacts:form'),
                                    {'email': 'test@example.com', 'content': 'This is a test question.'})
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful form submission

        # Check if the message was created in the database
        self.assertEqual(Message.objects.count(), 1)
        message = Message.objects.first()
        self.assertEqual(message.email, 'test@example.com')
        self.assertEqual(message.content, 'This is a test question.')

    def test_multiple_submissions_within_three_minutes(self):
        # Create a message in the database
        Message.objects.create(email='test@example.com', content='Test content', ip='127.0.0.1', verified=False)

        # Attempt to submit another message within three minutes
        response = self.client.post(reverse('contacts:form'),
                                    {'email': 'test@example.com', 'content': 'Another test question.'})
        self.assertEqual(response.status_code, 200)  # Expect a 200 response (in fact, this is error)

        # Check if an error message is present in the response
        self.assertContains(response, 'You are allowed to ask question only 1 time per 3 minutes.')

        # Check if the message count remains 1 in the database
        self.assertEqual(Message.objects.count(), 1)

    @freeze_time("2023-01-01 12:00:00")
    def test_ip_message_quantity_within_three_minutes(self):
        # Create a message in the database
        Message.objects.create(email='test@example.com', content='Test content', ip='127.0.0.1', verified=False)

        # Move time forward by 5 minutes
        with freeze_time("2023-01-01 12:05:00"):
            # Attempt to submit another message from the same IP
            response = self.client.post(reverse('contacts:form'),
                                        {'email': 'test@example.com', 'content': 'Another test question.'})
            self.assertEqual(response.status_code, 302)  # Expect a redirect after successful form submission

            # Check if the message count equal to 2 in the database (added new message)
            self.assertEqual(Message.objects.count(), 2)
