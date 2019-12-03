from django.shortcuts import HttpResponse, render, reverse
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
    #return HttpResponse('Page reserved for senators profiles')
    profiles = Profile.objects.order_by('political_party', 'state')
    context = {}

    democrats = Profile.objects.filter(political_party='D').order_by('state')
    context = {}

    republicans = Profile.objects.filter(political_party='R').order_by('state')
    context = {}

    independents = Profile.objects.filter(political_party='ID').order_by('state')
    context = {
                "profiles" : profiles,
                "independents" : independents,
                "democrats" : democrats,
                "republicans" : republicans,}


    return render(request, 'capstoneapp/profiles.html', context) 

#localhost:8000/about
def about(request):
    return HttpResponse('Page reserved for historical summary of US voting..chart showing voter participation from 1900 to present  ')

#localhost:8000/vote
def vote(request):
    return HttpResponse('Page reserved for voter registration form')

#localhost:8000/base
def base(request):
    #return HttpResponse('THIS IS THE BASE PAGE')
    return render(request, 'capstoneapp/base.html') 

#localhost:8000/charts
def charts(request):
    #return HttpResponse('THIS IS MY D3 PAGE')
    return render(request, 'capstoneapp/charts.html')

#localhost:8000/chartsmale
def chartsmale(request):
    #return HttpResponse('HISTORICAL ')
    return render(request, 'capstoneapp/chartsmale.html')

#localhost:8000/totalvotes
def totalvotes(request):
    #return HttpResponse('THIS IS TOTAL US VOTES')
    return render(request, 'capstoneapp/totalusvotes.html')

#localhost:8000/trendline
def trendline(request):
    #return HttpResponse('HISTORICAL ')
    return render(request, 'capstoneapp/trendline.html')


#localhost:8000/base
def about(request):
    #return HttpResponse('ABOUT PAGE ')
    return render(request, 'capstoneapp/about.html')