import os

# Module for reading CSV files
import csv

# Module for statistics calculations
import statistics

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
  
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    net_total = 0
    row_count = 0

    diffs_list = []
    month_list = []
    last_pl = 0

    
    # Read each row of data after the header
    for row in csvreader:
        row_count = row_count + 1
        net_total = net_total + int(row[1])
        month_list.append(row[0])

        #current_pl = int(row[1])
        
        if row_count > 1:
            diff_pl = int(row[1]) - last_pl
            diffs_list.append(diff_pl)

            #print(diff_pl)
            #print(f"Rowcount is {row_count}, PL is {int(row[1])}, Last PL is {last_pl}")
        
        last_pl = int(row[1])
        
    max_diff = max(diffs_list)
    min_diff = min(diffs_list)

    max_diff_row = diffs_list.index(max(diffs_list))
    min_diff_row = diffs_list.index(min(diffs_list))

    max_diff_month = month_list[max_diff_row]
    min_diff_month = month_list[min_diff_row]

 

    print("Min row = " +str(min_diff_row))
    print("Max row = " +str(max_diff_row))

#print(diffs_list)
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${statistics.mean(diffs_list)}")
print(f"Greatest Increase in Profits: {max_diff_month} ${max(diffs_list)}")
print(f"Greatest Decrease in Profits: {min_diff_month} ${min(diffs_list)}")