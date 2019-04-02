from django import forms
from .models import Project, User
from django_select2.forms import Select2MultipleWidget


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['collaborators'].queryset = User.objects.exclude(username=user.username)
        self.fields['collaborators'].label_from_instance = self.label_from_instance

    class Meta:
        model = Project
        fields = ['name', 'collaborators', 'description']
        widgets = {'collaborators': Select2MultipleWidget()}

    @staticmethod
    def label_from_instance(obj: User):
        return obj.full_name()
