# File:     forest.py
# Author:   Brandon Poole
# Date:     March 19th, 2018
# Purpose:  Random Forest implementation with GloVe

import csv
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


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

toxic = []          # Index 2
severeToxic = []    # Index 3
obscene = []        # Index 4
threat = []         # Index 5
insult = []         # Index 6
identityHate = []   # Index 7

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
            # Length of vectors should be 50
            # We lose 262 cases from invalidy mapped GloVe vectors
            if(len(sentenceToVector[-1]) != 50):
                del sentenceToVector[-1]
            else:
                toxic.append(row[2])
                severeToxic.append(row[3])
                obscene.append(row[4])
                threat.append(row[5])
                insult.append(row[6])
                identityHate.append(row[7])
        

# === Random Forest Implementation ===

#Model Selection splitter for evaluation
X_train, X_test, y_train, y_test = train_test_split(sentenceToVector, toxic, test_size=0.33, random_state=42)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X_train, y_train)

# Evaluation

testData = clf.predict(X_test)
print(confusion_matrix(y_test, testData))


