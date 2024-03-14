from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from blog.utils import path_and_rename, file_size, allowed_content_types


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=200000)
    active = models.BooleanField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename, validators=[file_size, allowed_content_types])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Post)
def delete_old_image_on_model_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


@receiver(pre_save, sender=Post)
def delete_old_image_on_model_update(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image and old_instance.image != instance.image:
                old_instance.image.delete(False)
        except sender.DoesNotExist:
            pass
