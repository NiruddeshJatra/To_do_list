from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
  # path('', views.show_tasks, name='show_tasks'),
  path('', views.showTasks.as_view(), name='show_tasks'),
  # path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
  path('completed_tasks/', views.completedTasks.as_view(), name='completed_tasks'),
  path('complete/<int:pk>/', views.MarkTaskCompleted.as_view(), name='mark_task_completed'),
  # path('completed_tasks/<str:taskTitle>/', views.completed_tasks, name='mark_completed'),
  # path('add/', views.add_or_edit_task, name='add_task'),
  path('add/', views.addTask.as_view(), name='add_task'),
  # path('delete/<str:taskTitle>/', views.delete_task, name='delete_task'),
  path('delete/<int:pk>/', views.deleteTask.as_view(), name='delete_task'),
  # path('edit/<str:taskTitle>/', views.add_or_edit_task, name='edit_task'),
  path('edit/<int:pk>/', views.updateTask.as_view(), name='edit_task'),
]