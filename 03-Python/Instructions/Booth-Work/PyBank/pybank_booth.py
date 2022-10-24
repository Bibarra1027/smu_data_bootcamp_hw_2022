import csv

csvpath = "Resources/budget_data.csv"

rows = 0
total = 0

last_profit = 0
tot_changes = 0
num_changes = 0 # expected to be 85

max_change = -999999999
min_change = 999999999
min_month = ""
max_month = ""

with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # print(row)
        rows += 1
        total += int(row[1])

        # calculate the changes
        if rows != 1:
            change = int(row[1]) - last_profit
            tot_changes += change
            num_changes += 1

            # find max/min of change
            if (change > max_change):
                max_change = change
                max_month = row[0]
            elif (change < min_change):
                min_change = change
                min_month = row[0]
            else:
                pass

        # Always do this bit
        # reset
        last_profit = int(row[1])

avg_change = tot_changes / num_changes
# print(rows)
# print(total)
# print(num_changes)
# print(avg_change)
# print(f"Max Change: {max_month}: {max_change}")
# print(f"Min Change: {min_month}: {min_change}")

output = f"""Financial Analysis
----------------------------
Total Months: {rows}
Total: ${total}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: Feb-14 (${min_change})"""

print(output)

with open('pybank_out_booth.txt', 'w') as f:
    f.write(output)