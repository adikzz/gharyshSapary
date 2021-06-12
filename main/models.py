from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=500)
    password = models.CharField(max_length=64)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
