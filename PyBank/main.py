#Dependencies
import os
import csv

#define variables
months = []
profit_loss_changes = []

month_count = 0
prof_loss = 0
previous_month_pl = 0
current_month_pl = 0
change_pl = 0

#specify the file to open
pybank_csv = os.path.join('..', "Resources", 'budget_data.csv')

#Open the file using 'read' mode. Specify the variable to hold the contents
with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header
    next(csvreader, None)
    for row in csvreader:

        #calculate row count
        month_count += 1
        #calculate Profit/Losses over entire period
        current_month_pl = int(row[1])
        change_pl += current_month_pl

        if(month_count == 1):
            #make value of previous month equal to current month
            previous_month_pl = current_month_pl
            continue
        else:
            #calculate change in profit/losses
            change_pl = current_month_pl - previous_month_pl
            #append each month to the months[]
            months.append(row[0])
            #append each change of profit/loss to profit_loss_changes
            profit_loss_changes.append(change_pl)
            #make current change in profit/loss equal to previous change profit/loss for the next loop
            previous_month_pl = current_month_pl

    #calculate sum of changes in profit/loss  
    sum_change_pl = sum(profit_loss_changes)
    # calculcate average change in profit/loss
    avg_change_pl = round(sum_change_pl/(month_count -1), 2) 

    #calculate greatest increase/decrease in profits
    high_change = max(profit_loss_changes)
    low_change = min(profit_loss_changes)

    #locate index value of highest and lowest changes in profit/loss
    high_month_index = profit_loss_changes.index(high_change)
    low_month_index = profit_loss_changes.index(low_change)

    #link index to actual month in data
    high_month = months[high_month_index]
    low_month = months[low_month_index]

#Print Headings
print("Financial Analysis")
print("--------------------------")
#Print out analysis
print(f"Total Months: {month_count}")    
print(f"Total: ${prof_loss}")    
print(f"Average Change: ${avg_change_pl}")
print(f"Greatest Incerase in Profits: {high_month} (${high_change})")
print(f"Greatest Decrease in Profits: {low_month} (${low_change})")

#Write results into a text file
budget_file = os.path.join("..", "Analysis", 'budget_analysis.txt')
with open(budget_file, 'w') as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Months: {month_count}\n") 
    outfile.write(f"Total: ${prof_loss}\n")    
    outfile.write(f"Average Change: ${avg_change_pl}\n")
    outfile.write(f"Greatest Incerase in Profits: {high_month} (${high_change})\n")
    outfile.write(f"Greatest Decrease in Profits: {low_month} (${low_change})\n")


  


       

