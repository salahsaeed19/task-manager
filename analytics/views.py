from django.shortcuts import render
from tasks.models import Task
from django.db.models import Count

def dashboard_view(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks

    priority_distribution = Task.objects.values('priority').annotate(count=Count('priority'))

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'priority_distribution': priority_distribution,
        'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
    }
    return render(request, 'analytics/dashboard.html', context)
