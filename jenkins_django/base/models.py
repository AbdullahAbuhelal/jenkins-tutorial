from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)
    author = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title