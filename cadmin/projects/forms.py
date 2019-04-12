from django import forms
from .models import Project, User
from django_select2.forms import Select2MultipleWidget


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['primary_investigators'].label_from_instance = self.label_from_instance
        self.fields['research_assistants'].label_from_instance = self.label_from_instance

    class Meta:
        model = Project
        fields = [
            'name', 'description', 'primary_investigators', 'research_assistants', 'has_irb_cert',
            'external_irb_approval', 'protocol', 'instructions', 'is_no_deception', 'has_grant_funding', 'grant_agency',
            'grant_funds_released', 'alt_source_funding'
              ]
        widgets = {'primary_investigators': Select2MultipleWidget(), 'research_assistants': Select2MultipleWidget}

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super(Project, self).__init__(*args, **kwargs)
            if not user.is_irbadmin:
                del self.fields['approved']


    @staticmethod
    def label_from_instance(obj: User):
        return obj.full_name()
