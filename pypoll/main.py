
#PyPoll homework exercise main file

import os

# Module for reading CSV files
import csv

voter_id_list = []
county_list = []
candidate_list = []

csvpath = os.path.join('..', 'Resources', 'election_data_test.csv')
  
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    voter_id_list
    # Read each row of data after the header
    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

        row_counter = len(set(candidate_list))

     #unique_candidates = set(candidate_list)
       
    # Print results to screen
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(voter_id_list)}")
    print("-------------------------")
    for row in set(candidate_list):
        print(row)


    

