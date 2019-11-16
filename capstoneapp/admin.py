from django.contrib import admin

# Register your models here.
from .models import Profile, DataSet

admin.site.register(Profile)
admin.site.register(DataSet)
