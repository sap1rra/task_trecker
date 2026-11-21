from django.db import models

# Create your models here.   
class Task(models.Model):
    STATUS_CHOISES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    PRIORITY_CHOISES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISES, default='medium')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    executors = models.ManyToManyField('auth.User', related_name='assigned_tasks', blank=True)

    def __str__(self):
        return f"{self.title} - {self.status} - {self.priority}"
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    
class Meta:
    ordering= ['-updated_at', '-created_at']
    
    
#class User(models.Model):
    #username = models.CharField(max_length=50)
   # email = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)