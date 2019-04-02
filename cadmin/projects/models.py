from django.db import models
from profiles.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name='projects', blank=True)

    def __str__(self):
        return self.name
