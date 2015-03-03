from django.forms import ModelForm
from berth.project.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'slug', 'repo_url']
