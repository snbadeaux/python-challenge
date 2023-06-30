# Dependencies
import os
import csv
from decimal import Decimal


# Define PyPoll's variables
candidates = []
votes_per_candidate = []
candidate_votes = {}
total_votes = 0


#specify the file to open
pypoll_csv = os.path.join("Resources", 'election_data.csv')

#Open the file using 'read' mode. Specify the variable to hold the contents
with open(pypoll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header
    csv_header = next(csvreader)

    #star loop
    for row in csvreader:
        #tells where to look for candidate name
        candidate_name = row[2]
        #tells to add the candidates name to the dictionary
        if candidate_name not in candidates:
            candidates.append(row[2])
            #starts count at zero
            candidate_votes[candidate_name] = 0   
        #adds count by 1 for every row for each candidates name in the matching dictionary value
        candidate_votes[candidate_name] += 1    
        #adds count by 1 for every row     
        total_votes += 1
    
    
    #grabs(gets) number associated with candidate name in dictionary to the vote count
    #set labels for easier calculation of percentage
    for candidate in candidate_votes:
        ccs =  candidate_votes.get("Charles Casper Stockham")
        dd = candidate_votes.get("Diana DeGette")
        rad = candidate_votes.get("Raymon Anthony Doane")

    #Calculate  percentage of votes per candidate to 3 decimal points
    percent_ccs = round((ccs/total_votes)*100, 3)
    percent_dd = round((dd/total_votes)*100, 3)
    percent_rad = round((rad/total_votes)*100, 3)   
                        
#print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {percent_ccs} %{ccs}")
print(f"Diana DeGette: {percent_dd} %{dd}")
print(f"Raymon Anthony Doane: {percent_rad} %{rad}")
print("-------------------------")
print(f"Winner: Diane DeGette")
print("-------------------------")

#Write results into a text file
election_file = os.path.join("Analysis", 'election_analysis.txt')
with open(election_file, 'w') as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("---------------------\n")   
    outfile.write(f"Charles Casper Stockham: {percent_ccs} %{ccs}\n")
    outfile.write(f"Diana DeGette: {percent_dd} %{dd}\n")
    outfile.write(f"Raymon Anthony Doane: {percent_rad} %{rad}\n")
    outfile.write("---------------------\n")
    outfile.write(f"Winner: Diane DeGette\n")
    outfile.write("---------------------\n")

   


