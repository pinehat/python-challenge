# Module for finding/creating files
import os

# Module for reading delimited files
import csv

# Module for statistics calculations
import statistics

# Define input and output files
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join("budget_analysis.txt")
  
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # define variable to increment total profits over period
    net_total = 0
    # define variable to count number of records (months)
    row_count = 0

    # list to keep track of the change in profits each month
    diffs_list = []
    # list to store all records' months
    month_list = []

    # Define variable to store each month's profit change as we process.
    last_pl = 0

    # Read each row of data after the header.
    for row in csvreader:
        # increment row counter
        row_count = row_count + 1
        # accrue profits/losses
        net_total = net_total + int(row[1])      
        # Starting with second row of data, add month to month list. Append to diffs_list
        #   the difference between this month's and last month's profits.
        if row_count > 1:
            month_list.append(row[0])
            diffs_list.append(int(row[1]) - last_pl)

            #print(str(int(row[1]) - last_pl))
            #print(f"Rowcount is {row_count}, PL is {int(row[1])}, Last PL is {last_pl}")
        
        # store current row's profit/loss for next iteration
        last_pl = int(row[1])
 
    # Find the row number for which the change in profits was the greatest and the least.
    max_diff_row = diffs_list.index(max(diffs_list))
    min_diff_row = diffs_list.index(min(diffs_list))

    # Using row numbers found above, find the corresponding months in the month_list for max & min.
    max_diff_month = month_list[max_diff_row]
    min_diff_month = month_list[min_diff_row]

    # Reformat max and min months for screen and output file
    month_split = max_diff_month.split("-")
    max_diff_month = month_split[0] + "-20" + month_split[1]
    month_split = min_diff_month.split("-")
    min_diff_month = month_split[0] + "-20" + month_split[1]
    #print("Min row = " +str(min_diff_row))
    #print("Max row = " +str(max_diff_row))

# Find and store the average monthly change in profits
average_change = statistics.mean(diffs_list)

# Find and store the max and min profit changes over the months
greatest_increase = max(diffs_list)
greatest_decrease = min(diffs_list)

# Define function to format currency results as $0,000.00
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# Print results to the screen
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Profits and losses over {row_count} months")
print(f"Total Profits: {as_currency(net_total)}")
print(f"Average Monthly Change: {as_currency(average_change)}")
print(f"Greatest Increase in Profits: {max_diff_month} {as_currency(greatest_increase)}")
print(f"Greatest Decrease in Profits: {min_diff_month} {as_currency(greatest_decrease)}")

# Write results to output file budget_analysis.txt
with open(output_path, "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("---------------------------" + "\n")
    text.write(f"Profits and losses over {row_count} months" + "\n")
    text.write(f"Total Profits: {as_currency(net_total)}" + "\n")
    text.write(f"Average Monthly Change: {as_currency(average_change)}" + "\n")
    text.write(f"Greatest Increase in Profits: {max_diff_month} {as_currency(greatest_increase)}" + "\n")
    text.write(f"Greatest Decrease in Profits: {min_diff_month} {as_currency(greatest_decrease)}" + "\n")
