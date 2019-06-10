import os

# Module for reading CSV files
import csv

# Module for statistics calculations
import statistics

csvpath = os.path.join('..', 'Resources', 'k.csv')
  
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    net_total = 0
    row_count = 0
    diffs_list = []
    last_pl = 0
    
    # Read each row of data after the header
    for row in csvreader:    
        print(str(row_count))
        net_total = net_total + int(row[1])
        if row_count != 0:
            diff_pl = int(row[1]) - last_pl
            diffs_list.append(diff_pl)
        
        last_pl = int(row[1])
        row_count = row_count + 1

print(diffs_list)
my_mean = statistics.mean(diffs_list)
print("mean = " + str(my_mean))
max_diff = max(diffs_list)
print("max diff = " + str(max_diff))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: {net_total}")
print(f"Average Change: {statistics.mean(diffs_list)}")
print(f"Greatest Increase in Profits: {max(diffs_list)}")
print(f"Greatest Decrease in Profits: {min(diffs_list)}")