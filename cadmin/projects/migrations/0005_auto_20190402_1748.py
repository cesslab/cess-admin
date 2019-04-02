# Generated by Django 2.1.7 on 2019-04-02 17:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
