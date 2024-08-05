from django.shortcuts import render
from task_manager.models import Task


def task_list(request):
    tasks = Task.objects.all()

    return render(request, 'task_list.html', {'tasks': tasks})
