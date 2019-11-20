from django.shortcuts import HttpResponse, render
from .models import DataSet, Profile
from django.utils import timezone 

#Purpose of a view is to connect models and templates.  
#Supports taking content (models saved in database) and display in template
#In views, decide what model I want displayed in template
#Take the models I want to display and pass them to a template 

#localhost:8000/index
def index(request):
    return HttpResponse('Page reserved for the Map!')

#localhost:8000/census
def census(request):
    #return HttpResponse('Page reserved for census data ')
    data = DataSet.objects.all()
    context = {
        "data":data #variable in the loop statement needs to match this, in this case needs to match "data"
    }
    return render(request, 'capstoneapp/census.html', context) 

#localhost:8000/profiles
def profiles(request):
    return HttpResponse('Page reserved for senators profiles')
    
#localhost:8000/about
def about(request):
    return HttpResponse('Page reserved for historical summary of US voting..chart showing voter participation from 1900 to present  ')

#localhost:8000/vote
def vote(request):
    return HttpResponse('Page reserved for voter registration form')