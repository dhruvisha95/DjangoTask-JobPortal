from django.contrib import admin

# Register your models here.
from .models import Company, JobPost

admin.site.register(Company)
admin.site.register(JobPost)
