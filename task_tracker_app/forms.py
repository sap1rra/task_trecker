from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 
              'priority', 'attachment', 'executors']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
        'priority': forms.Select(attrs={'class': 'form-control'}),
        'attachment': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        'executors': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    }

    
        