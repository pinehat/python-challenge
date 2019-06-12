import os

# Module for reading CSV files
import csv

# Module for statistics calculations
import statistics

csvpath = os.path.join('..', 'Resources', 'budget_data_test.csv')
  
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
        net_total = net_total + int(row[1])
    
        if row_count != 0:
            month_list.append(row[0])
            diff_pl = int(row[1]) - last_pl
            diffs_list.append(diff_pl)

            print(diff_pl)

            print(f"Rowcount is {row_count}, PL is {int(row[1])}, Last PL is {last_pl}")

            if int(row[1]) > last_pl:
                max_row = row_count
            if int(row[1]) < last_pl:
                min_row = row_count
        
        last_pl = int(row[1])
        row_count = row_count + 1

    print("Min row = " +str(min_row))
    print("Max row = " +str(max_row))

    #max_months = month_list(max_row)
    #print(f" max months = {max_months}")

    #for row in csvreader:
    #    if row[1] == max_p_and_l:
    
    #       max_month = row[0]
    #       print("found max month" + str(max_month))
        #if diffs_list[1] == min_p_and_l:
            #max_month = month_list[row]

#print(diffs_list)
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: {net_total}")
print(f"Average Change: {statistics.mean(diffs_list)}")
print(f"Greatest Increase in Profits: {max(diffs_list)}")
print(f"Greatest Decrease in Profits: {min(diffs_list)}")