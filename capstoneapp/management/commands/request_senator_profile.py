from django.core.management.base import BaseCommand
from capstoneapp.models import Profile
from datetime import datetime
from . import secrets
import requests
import re
import json

#received Key Error for term_end variable. term_start in Sunlight Congress API,  and image from wiklipedia

# Process: get values out of dictionary, use values to create an instance of your model, save your model

#python manage.py request_senator_profile #command that goes in command prompt
class Command(BaseCommand):

    def handle(self, *args, **options):
        Profile.objects.all().delete() #deletes records in database before each migration. W/o statement, the migrations will just append to existing data
        
        
        #requesting data from propublica, the API key is placed in headers
        response = requests.get('https://api.propublica.org/congress/v1/115/senate/members.json',  headers={"X-API-Key":"3sDNreokJVp2T8VaRkjH1IYfajWHFLhuOacgM8Qj"})
         
        #print(response.text)
        #return
        
        data = json.loads(response.text) 

        #retrieving values from a dictionary with multiple list of arrays
        #print(data['results'][0]['members'][0]['first_name']) #prints 1st name of person in 1st array

        # for member in data['results'][0]['members']: #returns all 
        #     print(member)
        #     member['first_name']

        
        for member in data['results'][0]['members']:
            #print(member)
            first_name =  (member['first_name'])
            print(first_name)
            last_name =  (member['last_name'])
            print(last_name)
            state =  (member['state'])
            print(state)
            political_party = (member['party'])
            print(political_party)
            next_election = (member['next_election']) 
            print (next_election)
            contact_url =  (member['url'])
            print(contact_url)

            profiles = Profile(
                                first_name = first_name,
                                last_name = last_name,
                                state = state,
                                political_party = political_party,
                                next_election = next_election,
                                contact_url = contact_url,
                              )
            profiles.save()



        

           

    
    
   


    