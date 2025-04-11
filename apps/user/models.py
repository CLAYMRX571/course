from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    about_me = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    password_reset = models.CharField(max_length=100, blank=True, null=True)
