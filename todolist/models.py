from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    explanation = models.TextField(blank=True, null=True)
    end = models. BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.title
# Create your models here.
