from django.test import TestCase
from projects.models import Project
from profiles.models import User


class TestProject(TestCase):

    def setUp(self):
        User.objects.create(
            username='peter',
            email='peter@gmail.com',
            first_name='Peter',
            last_name='First'
        )
        User.objects.create(
            username='john',
            email='john@gmail.com',
            first_name='John',
            last_name='Long'
        )
        self.project = Project.objects.create(
            name='PD',
            description='fdfdf',
            approved=True,
        )
        self.project.collaborators.set(User.objects.get())

    def test_project_collaborators(self):
        self.assertEqual(2, len(self.project.collaborators))
