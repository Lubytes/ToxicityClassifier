# File:     forest.py
# Author:   Brandon Poole
# Date:     March 19th, 2018
# Purpose:  Random Forest implementation with GloVe

import csv

# Make dictionaries out of vectors
dict = {}

vectors = open('../Input Data/Random Forest Data/vectors.txt', "r")
lines = list(vectors)
for line in lines:
    line = line.split()
    key = line[0]
    del line[0]
    line = list(map(float,line))
    dict[key] = line

# Find numerical representations for each comment using the vector mappings

sentenceToVector = []
invalidKeys = []

with open('../Input Data/train-edited.csv', encoding="utf8", newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if(row[1] != "commenttext"):
            wordMappings = []
            commentArray = row[1].split()
            for word in commentArray:
                try:
                    wordMappings.append(dict[word])
                except:
                    invalidKeys.append(word)
            sentenceToVector.append([sum(x) for x in zip(*wordMappings)])
        

