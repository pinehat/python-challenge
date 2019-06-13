import os

# Module for reading CSV files
import csv

# Module for statistics calculations
import statistics

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join("budget_analysis.txt")
  
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
        #month_list.append(row[0])
        
        if row_count > 1:
            month_list.append(row[0])
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

    #print("Min row = " +str(min_diff_row))
    #print("Max row = " +str(max_diff_row))

average_change = statistics.mean(diffs_list)
greatest_increase = max(diffs_list)
greatest_decrease = min(diffs_list)

def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

print("")
print("Financial Analysis")
print("----------------------------")
print(f"Data Over {row_count} Months")
print(f"Total Profits: {as_currency(net_total)}")
print(f"Average Monthly Change: {as_currency(average_change)}")
print(f"Greatest Increase in Profits: {max_diff_month} {as_currency(greatest_increase)}")
print(f"Greatest Decrease in Profits: {min_diff_month} {as_currency(greatest_decrease)}")

with open(output_path, "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("---------------------------" + "\n")
    text.write(f"Data over {row_count} months" + "\n")
    text.write(f"Total Profits: {as_currency(net_total)}" + "\n")
    text.write(f"Average Monthly Change: {as_currency(average_change)}" + "\n")
    text.write(f"Greatest Increase in Profits: {max_diff_month} {as_currency(greatest_increase)}" + "\n")
    text.write(f"Greatest Decrease in Profits: {min_diff_month} {as_currency(greatest_decrease)}" + "\n")