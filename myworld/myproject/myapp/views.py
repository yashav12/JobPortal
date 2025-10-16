from django.shortcuts import render,HttpResponse,redirect
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
        experience=req.POST.get("experience")
        qualification=req.POST.get("qualification")
        salary=req.POST.get("salary")
        skills=req.POST.get("skills")
        description=req.POST.get("description")
        companyName=req.POST.get("companyName")
        website=req.POST.get("website")

        if (len(title)==0 or len(location)==0 or len(jobtype)==0 or len(category)==0 or len(experience)==0 
            or len(qualification)==0 or len(salary)==0 or
            len(skills)==0 or len(description)==0 or len(companyName)==0 or len(website)==0):
            return redirect('/post a job')

        job=Job(title=title,location=location,jobtype=jobtype,category=category,
                experience=experience,qualification=qualification,salary=salary,skills=skills,description=description,
                companyName=companyName,website=website)
        job.save()
    return redirect("/")

def confirm(req):
    if req.method=="POST":
        fname=req.POST.get("fname")
        lname=req.POST.get("lname")
        phoneno=req.POST.get("phoneno")
        email=req.POST.get("email")
        message=req.POST.get("message")

        if (len(fname)==0 or len(lname)==0 or len(phoneno)==0 or len(email)==0 or len(message)==0):
            return redirect('/contact us')
        
        confirm=Confirm(fname=fname,lname=lname,phoneno=phoneno,email=email,message=message)
        confirm.save()
    return redirect("/")

def description(req):
    return render(req,'message.html')

def registration(req):
    return render(req,'login.html')


def user(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        email=req.POST.get("email")

        if (len(username)==0 or len(password)==0 or len(email)==0):
            return redirect('/log in')

        user=User(username=username,password=password,email=email)
        user.save()
    return redirect('/')
from django.db.models import Q

def search(request):
    title = request.POST.get('title', '').strip()
    location = request.POST.get('location', '').strip()
    jobtype = request.POST.get('jobtype', '').strip()

    jobs = Job.objects.all()

    if title:
        jobs = jobs.filter(title__icontains=title)
    
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    if jobtype:
        jobs = jobs.filter(jobtype__iexact=jobtype)  # Exact match, case-insensitive

    context = {
        'jobs': jobs,
        'title': title,
        'location': location,
        'jobtype': jobtype,
        'result_count': jobs.count()
    }

    return render(request, 'search.html', context)

def adminuser(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        email=req.POST.get("email")

        if (len(username)==0 or len(password)==0 or len(email)==0):
            return redirect('/log in')

        user=User(username=username,password=password,email=email)
        user.save()
    return redirect('/')

def Adminjob(req):
    if req.method=="POST":
        title=req.POST.get("title")
        location=req.POST.get("location")
        jobtype=req.POST.get("jobtype")
        category=req.POST.get("category")
        salary=req.POST.get("salary")
        skills=req.POST.get("skills")
        companyName=req.POST.get("companyName")
        website=req.POST.get("website")

        if (len(title)==0 or len(location)==0 or len(jobtype)==0 or len(category)==0 or len(salary)==0 or
             len(skills)==0 or len(companyName)==0 or len(website)==0):
            return redirect('/post a job')

        job=Job(title=title,location=location,jobtype=jobtype,category=category,
                salary=salary,skills=skills,companyName=companyName,website=website)
        job.save()
    return redirect("/")

   