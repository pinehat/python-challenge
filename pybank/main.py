#Python Homework - PyBank

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    net_total = 0
    row_count = 0

    # Read each row of data after the header
    for row in csvreader:
        row_count = row_count + 1
        net_total = net_total + int(row[1])
    print(str(net_total))

    #for i, l in enumerate(csvreader):
    #    pass
    
    print("Financial Analysis")
    print("----------------------------")
    #print(f"Total Months: {i + 1}")
    print(f"Total Months: {row_count}")
    print(f"Total: {net_total}")



    
