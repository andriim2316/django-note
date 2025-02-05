from django.test import TestCase
from django.urls import reverse
from django_note_app.models import Task, Category
from django.utils import timezone
from datetime import datetime
import pytz
class TaskViewTests(TestCase):
    def setUp(self):

        self.category = Category.objects.create(title='Work') #create a test category

    def test_create_task(self):
        deadline = timezone.make_aware(datetime(2025, 2, 3, 0, 0), pytz.UTC)
        response = self.client.post(reverse('show_all_tasks'), {
            'name': 'Test Task',
            'priority': 'high',
            'status': 'started',
            'deadline': deadline,
            'assignee': 'John Doe',
            'category': self.category.id
        })



        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.first()

        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.priority, 'high')
        self.assertEqual(task.status, 'started')
        self.assertEqual(task.deadline, timezone.make_aware(datetime(2025, 2, 3, 0, 0), pytz.UTC))
        self.assertEqual(task.assignee, 'John Doe')
        self.assertEqual(task.category, self.category)
        self.assertRedirects(response, reverse('show_all_tasks'))


    def test_edit_task(self):
        # Create a task to edit
        task = Task.objects.create(
            name='Old Task',
            priority='low',
            status='not-started',
            deadline=timezone.now(),
            assignee='Jane Doe',
            category=self.category
        )

        updated_deadline = timezone.make_aware(datetime(2025, 2, 3, 0, 0), pytz.UTC)
        # Simulate editing the task
        response = self.client.post(reverse('edit_task', args=[task.id]), {
            'name': 'Updated Task',
            'priority': 'urgent',
            'status': 'finished',
            'deadline': updated_deadline,  # New deadline
            'assignee': 'John Smith',  # New assignee
            'category': self.category.id
        })

        task.refresh_from_db()

        # Check if task details were updated correctly
        self.assertEqual(task.name, 'Updated Task')
        self.assertEqual(task.priority, 'urgent')
        self.assertEqual(task.status, 'finished')
        self.assertEqual(task.deadline, updated_deadline)
        self.assertEqual(task.assignee, 'John Smith')
        self.assertEqual(task.category, self.category)

        self.assertRedirects(response, reverse('show_all_tasks'))