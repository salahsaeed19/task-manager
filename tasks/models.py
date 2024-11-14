from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail


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

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail(
                subject=f'New Task Assigned: {self.title}',
                message=f'Hello {self.user.username},\n\nYou have a new task assigned to you: "{self.title}".\n\nDescription: {self.description}\n\nDue Date: {self.due_date}\n\nThank you.',
                from_email='your-email@example.com',
                recipient_list=[self.user.email],
                fail_silently=False,
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey('Task', related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"