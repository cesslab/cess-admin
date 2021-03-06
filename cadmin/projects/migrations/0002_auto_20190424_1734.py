# Generated by Django 2.1.7 on 2019-04-24 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperimentInstructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='instructions',
        ),
        migrations.AlterField(
            model_name='project',
            name='primary_investigators',
            field=models.ManyToManyField(blank=True, related_name='pi_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='research_assistants',
            field=models.ManyToManyField(blank=True, related_name='ra_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimentinstructions',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
