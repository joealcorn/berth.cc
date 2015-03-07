from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView, UpdateView

from berth.mixins import LoginRequired
from berth.project.forms import ProjectForm
from berth.project.models import Project


class CreateProject(LoginRequired, FormView):
    template_name = 'project/new.html'
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()
        self.success_url = project.get_absolute_url()
        return super(CreateProject, self).form_valid(form)


class ProjectUpdate(LoginRequired, UpdateView):
    model = Project
    fields = ['name', 'slug', 'repo_url']
    template_name = 'project/project.html'

    def get_object(self):
        pk = self.kwargs[self.pk_url_kwarg]
        project = get_object_or_404(Project, pk=pk)
        if project.owner_id != self.request.user.id:
            raise PermissionDenied
        return project
