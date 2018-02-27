# File:     inputClean.py
# Author:   Brandon Poole
# Date:     February 27th, 2018
# Purpose:  To clean the Wikipedia test & training input data

import csv

# ID, Comment, Toxic, Severely Toxic, Obscene, Threat, Insult, Identity Hate
data = []

# Open original training data
with open('train.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row[1] = row[1].strip("\"") 
        row[1] = row[1].replace("\n"," ")

        data.append(row)


with open('train-edited.csv', 'w', encoding="utf8") as csvfile:
    fieldnames = ['id', 'comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')

    #hold = next(dataIter)
    #writer.writeheader()
    for i in data:
        writer.writerow({'id': i[0], 'comment_text': i[1], 'toxic': i[2], 'severe_toxic': i[3], 'obscene': i[4], 'threat': i[5], 'insult': i[6], 'identity_hate': i[7]})



