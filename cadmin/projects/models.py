from django.db import models
from profiles.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
