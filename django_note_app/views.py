from django.shortcuts import redirect, render
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from .models import Task
from .forms import TaskForm

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()  # Fetch tasks from the database
        form = TaskForm()           # Load the form
        return render(request, 'note_app_templates/tasks.html', {'tasks': tasks, 'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        tasks = Task.objects.all()
        return render(request, 'note_app_templates/tasks.html', {'tasks': tasks, 'form': form})

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "note_app_templates/edit.html"
    success_url = reverse_lazy('show_all_tasks')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'note_app_templates/delete_task.html'
    success_url = reverse_lazy('show_all_tasks')