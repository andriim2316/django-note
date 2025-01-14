from django.http import HttpResponse
from django.shortcuts import render
from django_note_app.models import Task
# Create your views here.
def test_function(request):
    return HttpResponse("<h2>Welcome to note app</h2>")


def show_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, "note_app_templates/tasks.html",
                   context= {
                       "tasks": tasks
                   })