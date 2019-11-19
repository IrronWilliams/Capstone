from django.shortcuts import HttpResponse, render
from .models import DataSet, Profile


#localhost:8000/index
def index(request):
    return HttpResponse('Page reserved for the Map!')

#localhost:8000/census
def census(request):
    return HttpResponse('Page reserved for all census data ')

#localhost:8000/profiles
def profiles(request):
    return HttpResponse('Page reserved for senators profiles')
    
#localhost:8000/about
def about(request):
    return HttpResponse('Page reserved for historical summary of US voting..chart showing voter participation from 1900 to present  ')

#localhost:8000/vote
def vote(request):
    return HttpResponse('Page reserved for voter registration form')