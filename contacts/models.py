from django.db import models

# Create your models here.
class contact(models.Model):
    name  = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.TextField()
    message = models.TextField(max_length=70)
   
    
