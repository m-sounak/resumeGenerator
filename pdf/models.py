from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    about = models.TextField(max_length=1000)
    previousWork = models.TextField(max_length=1000)
