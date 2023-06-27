#Dependencies
import os
import csv

#specify the file to write to
csvpath = os.path.join('..', "Resources", 'budget_data.csv')

#Lists to store data
Change = []



#Open the file using 'read' mode. Specify the variable to hold the contents
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

        #Skip the header
        next(csvreader, None)

        
        # Add Change in Profits/Losses column
        #Change.append(row[2])

        #Determine Change 
        #Change = 


    def count(row:0):
        print(f'"Total Months:" + count')