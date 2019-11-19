from django.db import models
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 20)
    political_party = models.CharField(max_length=20)
    my_image = models.ImageField(upload_to='images/', null=True, blank=True)
    contact_url = models.CharField(max_length = 200, null=True, blank=True)
    next_election = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class DataSet(models.Model):
    state = models.CharField(max_length = 30) 
    population_total = models.IntegerField(null=True, blank=True) 
    registered_voters_total = models.IntegerField(null=True, blank=True) 
    registered_voters_percent = models.FloatField(null=True, blank=True) 
    total_voters = models.IntegerField(null=True, blank=True)
    total_voters_percent = models.FloatField(null=True, blank=True)
    males_population_total = models.IntegerField(null=True, blank=True)
    males_registered_total = models.IntegerField(null=True, blank=True)
    males_registered_percent = models.FloatField(null=True, blank=True)
    males_voted_total = models.IntegerField(null=True, blank=True)
    males_voted_percent = models.FloatField(null=True, blank=True)
    females_population_total = models.IntegerField(null=True, blank=True)
    females_registered_total = models.IntegerField(null=True, blank=True)
    females_registered_percent = models.FloatField(null=True, blank=True)
    females_voted_total = models.IntegerField(null=True, blank=True)
    females_voted_percent = models.FloatField(null=True, blank=True)
    white_population_total = models.IntegerField(null=True, blank=True)
    white_registered_total = models.IntegerField(null=True, blank=True)
    white_registered_percent = models.FloatField(null=True, blank=True)
    white_voted_total = models.IntegerField(null=True, blank=True)
    white_voted_percent = models.FloatField(null=True, blank=True)
    black_population_total = models.IntegerField(null=True, blank=True)
    black_registered_total = models.IntegerField(null=True, blank=True)
    black_registered_percent = models.FloatField(null=True, blank=True)
    black_voted_total = models.IntegerField(null=True, blank=True)
    black_voted_percent = models.FloatField(null=True, blank=True)
    asian_population_total = models.IntegerField(null=True, blank=True)
    asian_registered_total = models.IntegerField(null=True, blank=True)
    asian_registered_percent = models.FloatField(null=True, blank=True)
    asian_voted_total = models.IntegerField(null=True, blank=True)
    asian_voted_percent = models.FloatField(null=True, blank=True)
    hispanic_population_total = models.IntegerField(null=True, blank=True)
    hispanic_registered_total = models.IntegerField(null=True, blank=True)
    hispanic_registered_percent = models.FloatField(null=True, blank=True)
    hispanic_voted_total = models.IntegerField(null=True, blank=True)
    hispanic_voted_percent = models.FloatField(null=True, blank=True)
    age_18to24_population_total = models.IntegerField(null=True, blank=True)
    age_18to24_registered_total = models.IntegerField(null=True, blank=True)
    age_18to24_registered_percent = models.FloatField(null=True, blank=True)
    age_18to24_voted_total = models.IntegerField(null=True, blank=True)
    age_18to24_voted_percent = models.FloatField(null=True, blank=True)
    age_25to34_population_total = models.IntegerField(null=True, blank=True)
    age_25to34_registered_total = models.IntegerField(null=True, blank=True)
    age_25to34_registered_percent = models.FloatField(null=True, blank=True)
    age_25to34_voted_total = models.IntegerField(null=True, blank=True)
    age_25to34_voted_percent = models.FloatField(null=True, blank=True)
    age_35to44_population_total = models.IntegerField(null=True, blank=True)
    age_35to44_registered_total = models.IntegerField(null=True, blank=True)
    age_35to44_registered_percent = models.FloatField(null=True, blank=True)
    age_35to44_voted_total = models.IntegerField(null=True, blank=True)
    age_35to44_voted_percent = models.FloatField(null=True, blank=True)
    age_45to64_population_total = models.IntegerField(null=True, blank=True)
    age_45to64_registered_total = models.IntegerField(null=True, blank=True)
    age_45to64_registered_percent = models.FloatField(null=True, blank=True)
    age_45to64_voted_total = models.IntegerField(null=True, blank=True)
    age_45to64_voted_percent = models.FloatField(null=True, blank=True)
    age_65plus_population_total = models.IntegerField(null=True, blank=True)
    age_65plus_registered_total = models.IntegerField(null=True, blank=True)
    age_65plus_registered_percent = models.FloatField(null=True, blank=True)
    age_65plus_voted_total = models.IntegerField(null=True, blank=True)
    age_65plus_voted_percent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.state






# class DataSet(models.Model):
#     state = models.CharField(max_length = 30) 
#     population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     registered_voters_total = models.CharField(null=True, blank=True, max_length = 20) 
#     registered_voters_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     total_voters = models.CharField(null=True, blank=True, max_length = 20) 
#     total_voters_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     males_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     males_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     males_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     males_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     males_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     females_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     females_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     females_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     females_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     females_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     white_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     white_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     white_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     white_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     white_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     black_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     black_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     black_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     black_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     black_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     asian_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     asian_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     asian_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     asian_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     asian_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     hispanic_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     hispanic_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     hispanic_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     hispanic_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     hispanic_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_18to24_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_18to24_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_18to24_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_18to24_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_18to24_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_25to34_population_total =models.CharField(null=True, blank=True, max_length = 20) 
#     age_25to34_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_25to34_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_25to34_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_25to34_voted_percent = models.FloatField(null=True, blank=True)
#     age_35to44_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_35to44_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_35to44_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_35to44_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_35to44_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_45to64_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_45to64_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_45to64_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_45to64_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_45to64_voted_percent =models.CharField(null=True, blank=True, max_length = 20) 
#     age_65plus_population_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_65plus_registered_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_65plus_registered_percent = models.CharField(null=True, blank=True, max_length = 20) 
#     age_65plus_voted_total = models.CharField(null=True, blank=True, max_length = 20) 
#     age_65plus_voted_percent = models.CharField(null=True, blank=True, max_length = 20) 

#     def __str__(self):
#         return self.state










