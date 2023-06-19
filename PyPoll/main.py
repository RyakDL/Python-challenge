#Import modules to load and read csv file
import os
import csv

#load the csv file
file_to_load = os.path.join("election_data.csv")

#Create lists, define variables, set vote counter to zero
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

#Open csv file and read the header row
with open(file_to_load, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #For loop to add for conditional statement to tally votes by candidate
    for row in csvreader:
        #Sum votes in vote counter
        total_votes += 1 

        #If statement to add canditates to list and track candidates votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            #Add number of votes to list
            num_votes.append(1)
        else:
            #Otherwise add existing candidate's votes to list
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    #For loop to calculate and track percentage of votes
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        #Format percentage to 3rd decimal point with %.3f format
        percentage = "%.3f%%" % percentage
        #Add percentage of votes to list
        percent_votes.append(percentage)
    
    #Define winner from candidate list by max number of votes
    winner = max(num_votes)
    index = num_votes.index(winner)
    winner_candidate = candidates[index]

#Print data summary to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
#For loop to print complete list of candidates, percent votes and number of votes
for j in range(len(candidates)):
    print(f"{candidates[j]}: {str(percent_votes[j])} ({str(num_votes[j])})")
print("--------------------------")
#Print winner candidate
print(f"Winner: {winner_candidate}")
print("--------------------------")

# Export to txt file
output = open("output_PyPoll.txt", "w")

line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for j in range(len(candidates)):
    line = str(f"{candidates[j]}: {str(percent_votes[j])} ({str(num_votes[j])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner_candidate}")
line7 = "--------------------------"

#Write to text file
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))