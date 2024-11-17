from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.SET_NULL, null=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M',
        help_text="Task priority (Low, Medium, High)"
    )
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "task_notifications",
            {
                "type": "send_notification",
                "message": {
                    "title": self.title,
                    "completed": self.completed,
                    "action": "updated"
                }
            }
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey('Task', related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"