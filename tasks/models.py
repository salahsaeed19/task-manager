from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
