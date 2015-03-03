from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from berth.mixins import LoginRequired
from berth.project.forms import ProjectForm


class CreateProject(LoginRequired, FormView):
    template_name = 'project/new.html'
    form_class = ProjectForm

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.owner = self.request.user
        project.save()
        # self.success_url = reverse('project', args=[project.id])
        return super(CreateProject, self).form_valid(form)
