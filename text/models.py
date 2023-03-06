from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
now = timezone.now()


class TextModel(models.TextChoices):
    general = models.TextField()
    attachments = models.ManyToManyField('Attachment')
    end = models.CharField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')

    def __str__(self):
        return self.name


def text():
    return None


class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'
