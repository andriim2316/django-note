from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)



class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("normal", "Normal"),
        ("high", "High"),
        ("urgent", "Urgent"),
    ]
    STATUS_CHOICES = [
        ("not-started", "Not Started"),
        ("started", "Started"),
        ("on-pause", "On Pause"),
        ("finished", "Finished"),
    ]

    name = models.TextField(null=False)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='normal')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not-started')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    assignee = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

