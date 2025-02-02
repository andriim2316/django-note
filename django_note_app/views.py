from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django_note_app.models import Task
from django_note_app.forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = "note_app_templates/tasks.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_tasks')
        return self.get(request, form=form)

# View to Edit Tasks
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "note_app_templates/edit.html"
    success_url = reverse_lazy('show_all_tasks')