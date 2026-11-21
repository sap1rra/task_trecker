from django.shortcuts import redirect, render
from task_tracker_app.forms import TaskForm
from .models import Task, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        task_list = Task.objects.filter(author=self.request.user)
        return task_list

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        content = request.POST.get('content')
        #attachment = request.FILES.get('attachment')
        
        if content:
           task.comments.create(author=request.user, content=content)
        return redirect('task_detail', pk=task.pk)
        

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm
    
    def form_valid(self,form ):
        self.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm