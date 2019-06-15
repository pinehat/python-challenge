# Module for input/output
import os

# Module for reading CSV files
import csv

# Define variable to count rows (votes)
total_votes = 0

# Define dictionary to store the unique candidates and number of their votes
dict_cand_votes = {}
# Define dictionary to store percentage of votes each candidate got
dict_cand_percentage = {}

# Define variable to compare candidates' votes
winning_votes = 0

# Define input and output paths and files
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join("election_results.txt")

# Open input file as delimited file
with open(csvpath, newline='') as csvfile:
    # create readable record
    csvreader = csv.reader(csvfile, delimiter=',')
    # get the header out of the way
    csv_header = next(csvreader)

    # For each row of data, increment total votes, get the candidate and populate candidate dictionary,
    #  incrementing unique candidates' votes as we go
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in dict_cand_votes:
            dict_cand_votes[candidate] = dict_cand_votes[candidate] + 1
        else:
            dict_cand_votes[candidate] = 1

# Display results to screen
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# For each listing in candidate votes dictionary, compute candidates' vote percentages and
#  store in new dictionary, then compare candidates' votes to running total of winning votes
#  to wind up with the the winner. Then print each candidate's votes and percentage, and
#  finally the winner.
for cand, cand_votes in dict_cand_votes.items():
    dict_cand_percentage[cand] = cand_votes / total_votes
    if cand_votes > winning_votes:
        winning_votes = cand_votes
        winner = cand
    print(f"{cand}: {dict_cand_percentage[cand]:.0%} ({cand_votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write election results to output file election_results.txt
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