from django import forms
from .models import Project, User, FileItem
from django_select2.forms import Select2MultipleWidget
from crispy_forms.helper import FormHelper


class ProjectForm(forms.ModelForm):
    irb_approval_method = forms.ChoiceField(label='IRB approval method', choices=Project.IRB_APPROVAL_CHOICES)
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['primary_investigators'].label_from_instance = self.label_from_instance
        self.fields['research_assistants'].label_from_instance = self.label_from_instance

    class Meta:
        model = Project
        fields = [
            'name', 'description', 'primary_investigators', 'research_assistants', 'irb_approval_method', 'approved'
              ]
        widgets = {'primary_investigators': Select2MultipleWidget(), 'research_assistants': Select2MultipleWidget}

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super(Project, self).__init__(*args, **kwargs)
            # Remove admin fields if the user is a researcher
            if not user.is_irbadmin:
                del self.fields['approved']
                del self.fields['irb_approval_method']

    @staticmethod
    def label_from_instance(obj: User):
        return obj.full_name()


class FileItemForm(forms.ModelForm):
    class Meta:
        model = FileItem
        fields = ['file']


