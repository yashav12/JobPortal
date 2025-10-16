from django.shortcuts import render

# Create your views here.


def dashboard(req):
    return render(req,'Admnhome.html')

def create_user(req):
    return render(req,'admuser.html')

def create_job(req):
    return render(req,'admjob.html')