from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_researcher = models.BooleanField(default=True)
    is_irbadmin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class ResearcherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    has_irb_cert = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ResearcherProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_researcher_profile(sender, instance, **kwargs):
    instance.researcherprofile.save()
