from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

# Create your views here.
def show_tasks(request):
  tasks = TaskModel.objects.filter(is_completed=False).all()
  return render(request, "show_tasks.html", {"tasks": tasks})

def add_or_edit_task(request, taskTitle=None):
  task = get_object_or_404(TaskModel, taskTitle=taskTitle) if taskTitle else None
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect("todolist:show_tasks")
  else:
    form = TaskForm(instance=task)
      
  return render(request, "add_or_edit_task.html", {"form": form, "task": task})

def completed_tasks(request, taskTitle=None):
  if taskTitle:
    task = get_object_or_404(TaskModel, taskTitle=taskTitle)
    task.is_completed = True
    task.save()
  tasks = TaskModel.objects.filter(is_completed=True).all()
  return render(request, "completed_tasks.html", {"tasks": tasks})

def delete_task(request, taskTitle):
  task = get_object_or_404(TaskModel, taskTitle=taskTitle)
  task.delete()
  return redirect("todolist:show_tasks")
