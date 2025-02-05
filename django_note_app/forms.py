from django import forms
from django_note_app.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'assignee', 'priority', 'deadline', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'assignee': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }