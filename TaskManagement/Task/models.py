from django.db import models
from Authentication.models import RegistrationView

class Task(models.Model):
    P_CHOICES = (
        (1, 'LOW'),
        (2, 'Medium'),
        (3, 'High'),
    )
    
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority_choice = models.IntegerField(choices=P_CHOICES, blank=True)
    user = models.ForeignKey(RegistrationView, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
