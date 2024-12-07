from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import TaskModel
from .forms import TaskForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View

# Create your views here.
# def show_tasks(request):
#   tasks = TaskModel.objects.filter(is_completed=False).all()
#   return render(request, "show_tasks.html", {"tasks": tasks})

class showTasks(ListView):
  model = TaskModel
  template_name = 'show_tasks.html'
  queryset = TaskModel.objects.filter(is_completed=False).all()
  context_object_name = 'tasks'

# def add_or_edit_task(request, taskTitle=None):
#   task = get_object_or_404(TaskModel, taskTitle=taskTitle) if taskTitle else None
#   if request.method == "POST":
#     form = TaskForm(request.POST, instance=task)
#     if form.is_valid():
#       form.save()
#       return redirect("todolist:show_tasks")
#   else:
#     form = TaskForm(instance=task)
      
#   return render(request, "add_or_edit_task.html", {"form": form, "task": task})

class addTask(CreateView):
  model = TaskModel
  fields = '__all__'
  template_name = "task_form.html"
  success_url = reverse_lazy("todolist:show_tasks")
  
  
class updateTask(UpdateView):
  model = TaskModel
  fields = '__all__'
  template_name = "task_form.html"
  success_url = reverse_lazy("todolist:show_tasks")
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['task'] = self.object  # 'self.object' is the task being edited
      return context

# def completed_tasks(request, taskTitle=None):
#   if taskTitle:
#     task = get_object_or_404(TaskModel, taskTitle=taskTitle)
#     task.is_completed = True
#     task.save()
#   tasks = TaskModel.objects.filter(is_completed=True).all()
#   return render(request, "completed_tasks.html", {"tasks": tasks})

class completedTasks(ListView):
  model = TaskModel
  template_name = 'completed_tasks.html'
  queryset = TaskModel.objects.filter(is_completed=True).all()
  context_object_name = 'tasks'
  
  
class MarkTaskCompleted(View):
  def post(self, request, pk):
    # Mark the specific task as completed
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = True
    task.save()
    # Redirect to the CompletedTasksView
    return redirect("todolist:completed_tasks")


# def delete_task(request, taskTitle):
#   task = get_object_or_404(TaskModel, taskTitle=taskTitle)
#   task.delete()
#   return redirect("todolist:show_tasks")

class deleteTask(DeleteView):
  model = TaskModel
  success_url = reverse_lazy("todolist:show_tasks")
  
  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.object.delete()
    return redirect(self.success_url)