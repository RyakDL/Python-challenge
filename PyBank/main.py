#Import modules to load and read csv file
import os
import csv

#Load the csv file
file_to_load = os.path.join("budget_data.csv")

#Create lists, define values & set values to zero
total_months = 0
total_prolss = 0
value = 0
change = 0
dates = []
profits = []

#Open and read the CSV file
with open(file_to_load, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row
    csv_header = next(csvreader)

    #Read the first row, set total months and prolss
    first_row = next(csvreader)
    total_months += 1
    total_prolss += int(first_row[1])
    value = int(first_row[1])
    
    #For loop: Setting rows after header and first row
    for row in csvreader:
        #Add dates to row 0 
        dates.append(row[0])
        
        # Calculate the change in profit and add to row 1
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Sum the total number of months
        total_months += 1

        #Add the total net profit/loss over periods to row 1
        total_prolss = total_prolss + int(row[1])

    #Calculate the max increase in profits and date
    max_increase = max(profits)
    max_index = profits.index(max_increase)
    max_date = dates[max_index]

    #Calculate the maximum decline in profits and date 
    max_decrease = min(profits)
    decreased_index = profits.index(max_decrease)
    decreased_date = dates[decreased_index]

    #Define function to calculate average change in profits
    def average(numbers):
        length =len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total/length
    #Calculate average change in profits/losses between months over entire period
    average_chg = average(profits)
    
#Print data summary to terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_prolss)}")
print(f"Average Change: ${str(round(average_chg,2))}")
print(f"Greatest Increase in Profits: {max_date} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {decreased_date} (${str(max_decrease)})")

#Export to txt file
output = open("output_PyBank.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_prolss)}")
line5 = str(f"Average Change: ${str(round(average_chg,2))}")
line6 = str(f"Greatest Increase in Profits: {max_date} (${str(max_increase)})")
line7 = str(f"Greatest Decrease in Profits: {decreased_date} (${str(max_decrease)})")

#Write to txt file
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))