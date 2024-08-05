from django.urls import path
from task_manager.views import task_list


urlpatterns = [
    path('', task_list, name='task_list')
]