from django.contrib import admin

# Register your models here.
from .models import User, Project

admin.site.register(User)
admin.site.register(Project)
