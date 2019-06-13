#PyPoll homework exercise main file

# Module for input/output
import os

# Module for reading CSV files
import csv

total_votes = 0
dict_cand_votes = {}
dict_cand_percentage ={}
winning_votes = 0

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join("election_results.txt")

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # For each row, increment total votes and populate candidates dictionary
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in dict_cand_votes:
            dict_cand_votes[candidate] = dict_cand_votes[candidate] + 1
        else:
            dict_cand_votes[candidate] = 1

#print(f"dict_cand_votes is {dict_cand_votes}")
#print(f"dict_cand_votes.items is {dict_cand_votes.items()}")

# get candidates' percentage votes and the winner
for cand, cand_votes in dict_cand_votes.items():

    dict_cand_percentage[cand] = cand_votes / total_votes
    if cand_votes > winning_votes:
        winning_votes = cand_votes
        winner = cand

#print(f"dict_cand_percentage is {dict_cand_percentage}")

# Display results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for cand, cand_votes in dict_cand_votes.items():
    print(f"{cand}: {dict_cand_percentage[cand]:.0%} ({cand_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write election results to file
with open(output_path, "w") as text:
    text.write("Election Results" + "\n")
    text.write("---------------------------" + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write("---------------------------" + "\n")
    for cand, cand_votes in dict_cand_votes.items():
        text.write(f"{cand}: {dict_cand_percentage[cand]:.0%} ({cand_votes})" + "\n")
    text.write("---------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("---------------------------" + "\n")