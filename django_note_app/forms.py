from django import forms
from django_note_app.models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'assignee', 'priority', 'deadline', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter task name'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }