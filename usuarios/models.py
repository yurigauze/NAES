from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Adicione esta linha

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
