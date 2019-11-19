from django.core.management.base import BaseCommand
from capstoneapp.models import DataSet
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./capstoneapp/management/commands/Statistics.csv', newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: #process brings in the csv file. Associating each column of csv file to each column in model.  And aligns each row to a column. 
                #print(row['Black %Voted']) Once all columns have been matched, each row read/imported  
                state = row['\ufeffSTATE']
                population_total = row['State_Population_Total']
                registered_voters_total = row['Registered_Voters_Total']
                registered_voters_percent = row['%Registered_Total']
                total_voters = row['Total_Voters']
                total_voters_percent = row['Total_Voters%']
                males_population_total = row['Male_Population_Total']
                males_registered_total = row['Male_Registered_Voters_Total']
                males_registered_percent = row['Male_Registered_Voters%']
                males_voted_total = row['Male_Total_Voted']
                males_voted_percent = row['Male_%Voted']
                females_population_total = row['Female_Population_Total']
                females_registered_total = row['Female_Registered_Voters_Total']
                females_registered_percent = row['Female_Registered_Voters%']
                females_voted_total = row ['Female_Total_Voted']
                females_voted_percent = row ['Female_%Voted']
                white_population_total = row ['White_non-Hispanic_Population_Total']
                white_registered_total = row['White_non-Hispanic_Registered_Voters_Total']
                white_registered_percent = row ['White_non-Hispanic_%Voted']
                white_voted_total = row ['White_non-Hispanic_Total_Voted']
                white_voted_percent = row['White_non-Hispanic_%Voted']
                black_population_total = row['Black_Population_Total']
                black_registered_total = row['Black_Registered _Voters_Total']
                black_registered_percent = row['Black_Registered_Voters%']
                black_voted_total = row['Black_Total_Voted']
                black_voted_percent = row['Black_%Voted']
                asian_population_total = row['Asian_Population_Total']
                asian_registered_total = row['Asian_Registered_Voters_Total']
                asian_registered_percent = row['Asian_Registered_Voters%']
                asian_voted_total = row['Asian_Total_Voted']
                asian_voted_percent = row['Asian_%Voted']
                hispanic_population_total = row['Hispanic_Population_Total']
                hispanic_registered_total  =row['Hispanic_Registered_Voters_Total']
                hispanic_registered_percent =row['Hispanic_Registered_Voters%']
                hispanic_voted_total = row['Hispanic_Total_Voted']
                hispanic_voted_percent = row['Hispanic_%Voted']
                age_18to24_population_total = row['18-24_Population_Total']
                age_18to24_registered_total = row['18-24_Registered_Voters_Total']
                age_18to24_registered_percent = row['18-24_Registered_Voters%']
                age_18to24_voted_total = row['18-24_Total_Voted']
                age_18to24_voted_percent = row['18-24_%Voted']
                age_25to34_population_total = row['25-34_Population_Total']
                age_25to34_registered_total = row['25-34_Registered_Voters_Total']
                age_25to34_registered_percent = row['25-34_Registered_Voters%']
                age_25to34_voted_total = row['25-34_Registered_Voters_Total']
                age_25to34_voted_percent = row['25-34_%Voted']
                age_35to44_population_total = row['35-44_Population_Total']
                age_35to44_registered_total = row['35-44_Registered_Voters_Total']
                age_35to44_registered_percent = row['35-44_Registered_Voters%']
                age_35to44_voted_total = row['35-44_Total_Voted']
                age_35to44_voted_percent = row['35-44_%Voted']
                age_45to64_population_total = row['45-64_Population_Total']
                age_45to64_registered_total = row['45-64_Registered_Voters_Total']
                age_45to64_registered_percent = row['45-64_Registered_Voters%']
                age_45to64_voted_total = row['45-64_Total_Voted']
                age_45to64_voted_percent = row['45-64_%Voted']
                age_65plus_population_total = row['65+_Population_Total']
                age_65plus_registered_total = row['65+_Registered_Voters_Total']
                age_65plus_registered_percent = row['65+_Registered_Voters%']
                age_65plus_voted_total =row['65+_Total_Voted']
                age_65plus_voted_percent = row['65+_%Voted']
                
                #from the variables created above, which is a variable for each row in CSV file, taking those rows and saving to the model 
                metrics = DataSet(state=state,
                            population_total=population_total,
                            registered_voters_total=registered_voters_total,
                            registered_voters_percent=registered_voters_percent,
                            total_voters=total_voters,
                            total_voters_percent=total_voters_percent,
                            males_population_total=males_population_total,
                            males_registered_total=males_registered_total,
                            males_registered_percent=males_registered_percent,
                            males_voted_total=males_voted_total,
                            males_voted_percent=males_voted_percent,
                            females_population_total=females_population_total,
                            females_registered_total=females_registered_total,
                            females_registered_percent=females_registered_percent,
                            females_voted_total=females_voted_total,
                            females_voted_percent=females_voted_percent,
                            white_population_total=white_population_total,
                            white_registered_total=white_registered_total,
                            white_registered_percent=white_registered_percent,
                            white_voted_total=white_voted_total,
                            white_voted_percent=white_voted_percent,
                            black_population_total=black_population_total,
                            black_registered_total=black_registered_total,
                            black_registered_percent=black_registered_percent,
                            black_voted_total=black_voted_total,
                            black_voted_percent=black_voted_percent,
                            asian_population_total=asian_population_total,
                            asian_registered_total=asian_registered_total,
                            asian_registered_percent=asian_registered_percent,
                            asian_voted_total=asian_voted_total,
                            asian_voted_percent=asian_voted_percent,
                            hispanic_population_total=hispanic_population_total,
                            hispanic_registered_total=hispanic_registered_total,
                            hispanic_registered_percent=hispanic_registered_percent,
                            hispanic_voted_total=hispanic_voted_total,
                            hispanic_voted_percent=hispanic_voted_percent,
                            age_18to24_population_total=age_18to24_population_total,
                            age_18to24_registered_total=age_18to24_registered_total,
                            age_18to24_registered_percent=age_18to24_registered_percent,
                            age_18to24_voted_total=age_18to24_voted_total,
                            age_18to24_voted_percent=age_18to24_voted_percent,
                            age_25to34_population_total=age_25to34_population_total,
                            age_25to34_registered_total=age_25to34_registered_total,
                            age_25to34_registered_percent=age_25to34_registered_percent,
                            age_25to34_voted_total=age_25to34_voted_total,
                            age_25to34_voted_percent=age_25to34_voted_percent,
                            age_35to44_population_total=age_35to44_population_total,
                            age_35to44_registered_total =age_35to44_registered_total ,
                            age_35to44_registered_percent=age_35to44_registered_percent,
                            age_35to44_voted_total=age_35to44_voted_total,
                            age_35to44_voted_percent=age_35to44_voted_percent,
                            age_45to64_population_total=age_45to64_population_total,
                            age_45to64_registered_total=age_45to64_registered_total,
                            age_45to64_registered_percent=age_45to64_registered_percent,
                            age_45to64_voted_total=age_45to64_voted_total,
                            age_45to64_voted_percent=age_45to64_voted_percent,
                            age_65plus_population_total=age_65plus_population_total,
                            age_65plus_registered_total=age_65plus_registered_total,
                            age_65plus_registered_percent=age_65plus_registered_percent,
                            age_65plus_voted_total=age_65plus_voted_total,
                            age_65plus_voted_percent=age_65plus_voted_percent)
                metrics.save()

#saving instances of model


          



#class TodoItem(models.Model):
#    text = models.CharField()
#    timestamp = models.DateTimeField()


#todo_item = TodoItem(text='was the car', timestamp=timezone.now())
#todo_item.save()

#population_total = row['']