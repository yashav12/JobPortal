"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as my_appviews
from AdminDashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',my_appviews.home),
    path('job listings/',my_appviews.job_listings),
    path('contact us/',my_appviews.contact_us),
    path('post a job/',my_appviews.post_a_job),
    path('submit',my_appviews.submit),
    path('confirm',my_appviews.confirm),
    path("jobdesc",my_appviews.description),
    path("registration/",my_appviews.registration),
    path('usersubmit',my_appviews.user),
    path('dashboard',views.dashboard),
    path('create user',views.create_user),
     path('create job',views.create_job),
     path('search',my_appviews.search),
     path('adminjob',my_appviews.Adminjob),
     path('adminuser',my_appviews.adminuser)
]  

# modelname.objects.all()