from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Post


class BlogModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Post.objects.create(title='Test Post', content='Lorem ipsum dolor sit amet.', active=True, image='image.png',
                            admin=user, )

    def test_post_str_representation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(str(post), 'Test Post')

    def test_post_default_values(self):
        post = Post.objects.get(title='Test Post')
        self.assertIsNotNone(post.created_at)
        self.assertIsNotNone(post.updated_at)


class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='testuser')
        self.post = Post.objects.create(title='Test Post', content='Lorem ipsum dolor sit amet.', active=True,
                                        image='image.png', admin=user, )

    def test_index_view(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(self.post, response.context['posts'])

    def test_show_view(self):
        response = self.client.get(reverse('blog:show', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show.html')
        self.assertEqual(self.post, response.context['post'])

    def test_show_view_inactive_post(self):
        self.post.active = False
        self.post.save()
        response = self.client.get(reverse('blog:show', args=[self.post.id]))
        self.assertEqual(response.status_code, 404)


class BlogURLsTest(TestCase):
    def test_index_url_resolves(self):
        url = reverse('blog:index')
        self.assertEqual(url, '/')

    def test_show_url_resolves(self):
        url = reverse('blog:show', args=[1])
        self.assertEqual(url, '/blog/1')
