from django.db import models
from profiles.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name='projects', blank=True)
    instructions = models.FileField(upload_to='project/instructions')

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Project)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)