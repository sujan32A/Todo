from django.db import models

# Create your models here.
class Todo(models.Model): #class name = table name in database when models.Model is inherited
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)