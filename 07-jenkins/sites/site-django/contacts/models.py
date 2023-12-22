from django.db import models


class Message(models.Model):
    email = models.CharField(max_length=255)
    content = models.TextField(max_length=200000)
    ip = models.GenericIPAddressField()
    verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} / {self.ip}'
