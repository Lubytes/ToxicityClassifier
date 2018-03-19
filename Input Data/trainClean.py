# File:     inputClean.py
# Author:   Brandon Poole
# Date:     March 19th, 2018
# Purpose:  To clean the Wikipedia test & training input data

import csv
import re

# ID, Comment, Toxic, Severely Toxic, Obscene, Threat, Insult, Identity Hate
data = []
# Header comments (usernames?)
regexUsernames = re.compile(r"[=]+.+[=]+", re.IGNORECASE) 
# Punctuation between two characters
regexPuncSpace = re.compile(r"(?<=\w)\,(?=\w)|(?<=\w)\.(?=\w)|(?<=\w)\?(?=\w)|(?<=\w)\!(?=\w)|(?<=\w)\:(?=\w)|(?<=\w)\/(?=\w)", re.IGNORECASE) 
# Punctuation
regexPunc = re.compile(r"[,\.'\"=\!\?\`\~\;]", re.IGNORECASE) 
# IPv4 Addresses
regexIPs = re.compile(r"[\d]+\.[\d]+\.[\d]+\.[\d]+", re.IGNORECASE) 
# URLS Edited from: https://www.regextester.com/20
regexURLHelper = re.compile(r"(?<=\/)\s(?=\w)|(?<=\w)\s(?=\/)|(?<=:)\s(?=\/)", re.IGNORECASE) 
regexURL = re.compile(r"((http[s]?|ftp):\/)\/([^:\/\s]+)((\/\w+)*[\/]?)([\w\-\.]+[^#?\s]+)", re.IGNORECASE)
# White-listed characters
regexWhiteList = re.compile(r"[^A-Za-z0-9 -]") 


# Open original training data
with open('test.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row[1] = row[1].strip()
        row[1] = row[1].replace("\n"," ")
        row[1] = regexURLHelper.sub("",row[1])
        row[1] = regexURL.sub("",row[1])
        row[1] = regexUsernames.sub("",row[1])
        row[1] = regexIPs.sub("",row[1])
        row[1] = regexPuncSpace.sub(" ",row[1])
        row[1] = regexPunc.sub("",row[1])
        row[1] = regexWhiteList.sub("",row[1])
        data.append(row)


with open('test-edited.csv', 'w', encoding="utf8") as csvfile:
    fieldnames = ['id', 'comment_text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    #writer.writeheader()
    for i in data:
        writer.writerow({'id': i[0], 'comment_text': i[1]})



