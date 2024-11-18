from django.db import models

class TaskStatistics(models.Model):
    date = models.DateField(auto_now_add=True)
    total_tasks = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    pending_tasks = models.IntegerField(default=0)
