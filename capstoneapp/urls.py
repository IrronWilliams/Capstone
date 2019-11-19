from django.urls import path
from . import views

app_name = 'capstoneapp'
urlpatterns = [
path('index/', views.index, name='index'),
path('census/', views.census, name='census'),
path('profiles/', views.profiles, name='profiles'),
path('about/', views.about, name='about'),
path('vote/', views.vote, name='vote'),


]
