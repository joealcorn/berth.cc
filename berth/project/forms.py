from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from berth.project.models import Project


class SubdomainField(CharField):

    def __init__(self, **kwargs):
        kwargs.setdefault('max_length', 128)
        kwargs.setdefault('min_length', 3)
        super(SubdomainField, self).__init__(**kwargs)

    def clean(self, value):
        if value is not None:
            value = value.strip()

            if value.lower() in settings.RESERVED_SUBDOMAINS:
                raise ValidationError('Subdomain is reserved')

            try:
                value.decode('ascii')
            except UnicodeDecodeError:
                error = 'Subdomain can not contain non-ascii characters'
                raise ValidationError(error)

            if ' ' in value:
                raise ValidationError('Subdomain can not contain space')

        return super(SubdomainField, self).clean(value)


class ProjectForm(ModelForm):
    subdomain = SubdomainField()

    class Meta:
        model = Project
        fields = ['name', 'subdomain', 'slug', 'repo_url']
