import csv
# Load CSV
csvpath = os.path.join("Resources" , "election_data.csv")
with open(csvpath) as csvfile:

# Define variables
total_votes = 0
candidate_votes = {}

# Read the election_data.csv file
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Skip the header row
    next(csvreader)
   
    # Loop through each row in the csvreader object
    for row in csvreader:
        # Calculate the total number of votes cast
        total_votes += 1
       
        # Add up the votes for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    candidate_percentages[candidate] = percentage

# Find the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the election results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f'{candidate}: {percentage}% ({votes})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')
 #format the print for Election results 
with open( output_log_path, 'w') as file:
    print("Election Results",'\n')
    print("------------------------",'\n')
    print("Total Votes: ",votes, '\n') 
    print("------------------------",'\n') 
    
# Write to output file
    file.write("Election Results \n")
    file.write("------------------------\n")
    file.write("Total Votes: %d\n" % votes)
    file.write("------------------------\n")
