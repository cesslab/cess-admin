# Generated by Django 2.1.7 on 2019-04-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcherprofile',
            name='has_irb_cert',
            field=models.BooleanField(default=False),
        ),
    ]
