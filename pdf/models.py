from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    github = models.CharField(max_length=100)

    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    passyear = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=100)

    post = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    skills = models.TextField(max_length=1000)

    achievements = models.TextField(max_length=1000)

    extracurr = models.TextField(max_length=1000)
