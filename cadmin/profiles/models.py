from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_researcher = models.BooleanField(default=True)
    is_irbadmin = models.BooleanField(default=False)


