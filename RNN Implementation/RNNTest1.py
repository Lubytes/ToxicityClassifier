# File:     RNNTest1.py
# Author:   Brandon Poole & Jason Parsons
# Date:     March 19th, 2018
# Purpose:  First attempt at an RNN with our edited training data

import csv

# Open edited training data as input
with open('../Input Data/train-edited.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print("ey")