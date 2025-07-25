from django.db import models

# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    jobtype=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    salary=models.TextField(max_length=122)
    skills=models.CharField(max_length=122)
    companyName=models.CharField(max_length=122)
    website=models.TextField(max_length=122)
    def __str__(self):
        return self.title
        
class Confirm(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    phoneno=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    message=models.TextField(max_length=255)       
    def __str__(self):
        return self.username
    
class User(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return self.username