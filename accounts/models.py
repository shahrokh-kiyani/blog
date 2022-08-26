from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='ایمیل')
