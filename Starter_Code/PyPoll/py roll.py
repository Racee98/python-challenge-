import os
import csv

# Set file paths
election_csv = os.path.join("Resources", "election_data.csv")
text_results = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read CSV file
with open(election_csv, 'r') as election_data:
    election_results = csv.reader(election_data, delimiter=',')
    header = next(election_results)  # Skip header row

    # Count votes for each candidate
    for row in election_results:
        candidate = row[2]
        total_votes += 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and find the winner
winner_votes = 0
winner = ""
percentage_votes = {}
for candidate, votes in candidate_votes.items():
    percentage = votes / total_votes * 100
    percentage_votes[candidate] = round(percentage, 2)
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print Election Results
print("Election Results")
print("---------------------------------")
for candidate, percentage in percentage_votes.items():
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")

# Write Election Results to a text file
with open(text_results, 'w') as text_analysis:
    text_analysis.write("Election Results\n")
    text_analysis.write("---------------------------------\n")
    for candidate, percentage in percentage_votes.items():
        text_analysis.write(f"{candidate}: {percentage}% ({candidate_votes[candidate]})\n")
    text_analysis.write("---------------------------------\n")
    text_analysis.write(f"Winner: {winner}\n")
    text_analysis.write("---------------------------------")
