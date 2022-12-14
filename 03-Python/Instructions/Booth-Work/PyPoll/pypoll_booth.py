import csv

csvpath = "Resources/election_data.csv"

rows = 0
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # print(row)
        rows += 1
        candidate = row[2]

        # build candidate dictionary dynamically
        if candidate in votes.keys():
            votes[candidate] += 1
        else:
            votes[candidate] = 1

print(rows)

for x in votes.keys():
    print(x)
    print(f"{votes[x]} total votes which is {100*votes[x]/rows}%")
    print()

#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner = max(votes, key=votes.get)
# print(winner)

output = f"""Election Results
-------------------------
Total Votes: {rows}
-------------------------"""

for x in votes.keys():
    perc = round(100*votes[x]/rows, 3)
    newline = f"""
{x}: {perc}% ({votes[x]})"""

    output += newline

lastline = f"""
-------------------------
Winner: {winner}
-------------------------
"""

output += lastline
print(output)

output2 = f"""Election Results
-------------------------
Total Votes: {rows}
-------------------------
Charles Casper Stockham: {round(100*votes['Charles Casper Stockham']/rows, 3)}% ({votes['Charles Casper Stockham']})
Diana DeGette: {round(100*votes['Diana DeGette']/rows, 3)}% ({votes['Diana DeGette']})
Raymon Anthony Doane: {round(100*votes['Raymon Anthony Doane']/rows, 3)}% ({votes['Raymon Anthony Doane']})
-------------------------
Winner: {winner}
-------------------------
"""

with open('output/pypoll_out_booth.txt', 'w') as f:
    f.write(output2)