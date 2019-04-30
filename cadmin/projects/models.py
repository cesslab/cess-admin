from django.db import models
from profiles.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Project(models.Model):
    NYU = 'NYU'
    CESS = 'CES'
    EXTERNAL = 'EXT'
    IRB_APPROVAL_CHOICES = ((NYU, 'NYU'), (CESS, 'CESS'), (EXTERNAL, 'External'))
    name = models.CharField(max_length=255)
    description = models.TextField()
    primary_investigators = models.ManyToManyField(User, related_name="pi_projects", blank=True)
    research_assistants = models.ManyToManyField(User, related_name="ra_projects", blank=True)
    irb_approval_method = models.CharField(max_length=3, choices=IRB_APPROVAL_CHOICES, default=CESS)
    # protocol = models.CharField(max_length=255)
    # has_grant_funding = models.BooleanField()
    # grant_agency = models.CharField(max_length=255)
    # grant_funds_released = models.DateField()
    # alt_source_funding = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Admin Fields
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FileItem(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


@receiver(post_delete, sender=FileItem)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.file.delete(save=False)
