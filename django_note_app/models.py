from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "low"),
        ("normal", "normal"),
        ("high", "high"),
        ("urgent", "urgent"),
    ]
    STATUS_CHOICES = [
        ("not-started", "Not started"),
        ("started", "Started"),
        ("on-pause", "On pause"),
        ("finished", "Finished"),
    ]
    name = models.TextField(null=False, )
    priority = models.CharField(
        max_length=15,
        choices=PRIORITY_CHOICES,
        default='normal'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='not-started'
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    assignee = models.CharField(max_length=50)