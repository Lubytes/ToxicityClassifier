# File:     dataEvaluation.py
# Author:   Brandon Poole
# Date:     April 7th, 2018
# Purpose:  To determine the amounts of certain words being in toxic vs non-toxic comments

import csv

Toxic = 0
NonToxic = 0

# Open original training data
with open('train-edited.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row[1] = (row[1]).lower()
            if row[2] == "1" or row[3] == "1" or row[4] == "1" or row[5] == "1" or row[6] == "1" or row[7] == "1":
                Toxic +=  1
            else:
                NonToxic += 1

print(Toxic)
print(NonToxic)
