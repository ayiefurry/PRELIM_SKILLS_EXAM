#Rono,Ia Shaira A.
import json
import csv

with open('covid_cases.json','r') as json_file:
    ourjson = json.load(json_file)
#print(ourjson)

#Retrieve the date reported, countries and territories, number of cases, and deaths.
for i in ourjson['records']:
    print(i['dateRep'],i['countriesAndTerritories'],i['cases'],i['deaths'])

#Create a new CSV file and then save the retrieved data to the CSV file

#File name of the CSV file
file_name = "C_Skills.csv"
Header = ["Date Reported","Country and Territory","Number of Cases","Number of Deaths"]
#Load covid_cases.json file
#with open("covid_cases.json",r)

with open(file_name,"w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(Header)

    for x in ourjson["records"]:
        csv_file.writerow([x['dateRep'],x['countriesAndTerritories'],x['cases'],x['deaths']])
