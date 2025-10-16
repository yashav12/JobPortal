from django.db import models

# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    jobtype=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    experience=models.CharField(max_length=255,null=True)
    qualification=models.CharField(max_length=255,null=True)
    salary=models.TextField(max_length=255)
    skills=models.CharField(max_length=255)
    description=models.CharField(max_length=255,null=True)
    companyName=models.CharField(max_length=255)
    website=models.TextField(max_length=255)
    def __str__(self):
        return self.title
        
class Confirm(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phoneno=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    message=models.TextField(max_length=255)       
    def __str__(self):
        return self.fname
    
class User(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,null=True)
    def __str__(self):
        return self.username
    
class Adminjob(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    jobtype=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    salary=models.TextField(max_length=255)
    skills=models.CharField(max_length=255)
    companyName=models.CharField(max_length=255)
    website=models.TextField(max_length=255)
    def __str__(self):
        return self.title
    
class Adminuser(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    def __str__(self):
        return self.username