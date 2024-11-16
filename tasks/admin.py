from django.contrib import admin
from .models import Task, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'completed', 'due_date', 'user', 'category')
    list_filter = ('priority', 'completed', 'due_date', 'user', 'category')
    search_fields = ('title', 'description')


admin.site.register(Category)