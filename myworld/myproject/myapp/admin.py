from django.contrib import admin
from myapp.models import Job,Confirm,User

# Register your models here.
admin.site.register(Job)
admin.site.register(Confirm)
admin.site.register(User)