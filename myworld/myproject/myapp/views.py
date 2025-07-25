from django.shortcuts import render,HttpResponse
from myapp.models import Job,Confirm,User

# Create your views here.
def home(req):
    alljobs=Job.objects.all()
    context={
        "allJobs":alljobs
    }
    return render(req,'index.html',context)

def about(req):
    return render(req,'about.html')

def job_listings(req):
    return render(req,'job.html')

def contact_us(req):
    return render(req,'contact.html')

def post_a_job(req):
    return render(req,'post.html')

def submit(req):
    if req.method=="POST":
        title=req.POST.get("title")
        location=req.POST.get("location")
        jobtype=req.POST.get("jobtype")
        category=req.POST.get("category")
        salary=req.POST.get("salary")
        skills=req.POST.get("skills")
        companyName=req.POST.get("companyName")
        website=req.POST.get("website")
         
        # print(title,location,jobtype,category,
        #         salary,skills,companyName,website)

        job=Job(title=title,location=location,jobtype=jobtype,category=category,
                salary=salary,skills=skills,companyName=companyName,website=website)
        job.save()
    return HttpResponse("ok done")

def confirm(req):
    if req.method=="POST":
        username=req.POST.get("username")
        email=req.POST.get("email")
        phoneno=req.POST.get("phoneno")
        website=req.POST.get("website")
        message=req.POST.get("message")
        
        confirm=Confirm(username=username,email=email,phoneno=phoneno,website=website,message=message)
        confirm.save()
    return HttpResponse("successful")

def description(req):
    return render(req,'message.html')

def log_in(req):
    return render(req,'login.html')

def register(req):
    return render(req,'reg.html')

def user(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        user=User(username=username,password=password)
        user.save()
    return HttpResponse("success")