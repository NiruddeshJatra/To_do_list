from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
  path('', views.show_tasks, name='show_tasks'),
  path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
  path('completed_tasks/<str:taskTitle>/', views.completed_tasks, name='mark_completed'),
  path('add/', views.add_or_edit_task, name='add_task'),
  path('delete/<str:taskTitle>/', views.delete_task, name='delete_task'),
  path('edit/<str:taskTitle>/', views.add_or_edit_task, name='edit_task'),
]