from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    department = models.CharField(max_length=255)
    is_researcher = models.BooleanField(default=True)
    is_irbadmin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name + ' ' + self.last_name

