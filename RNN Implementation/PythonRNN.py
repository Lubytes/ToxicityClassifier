#PythonApplication1.py
#Written by: Jason Parsons

import tensorflow as tf
import pandas as pd
import csv
import skflow

#use pandas to read in the training and test sets and store them in variables
train = pd.read_csv('train-edited.csv')
test = pd.read_csv('test-edited.csv')

 #checks for NULL values in data set. Our data does not contain any, but this is kept here for safety's sake
train.isnull().any(),test.isnull().any()  

#split the training set to seperate the features from the class labels
#The training set has 6 different class labels and one set of features (the comments)
classLabels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
y = train[classLabels].values
trainComments = train["commenttext"]
testComments = test["commenttext"]

#set the vocabulary and embedding sizes. Values chosen based on what is used in the official TensorFlow
#Word2Vec tutorial with modifications based on how many unique words we've found in our data set (with padding)
vocabularySize = 51000
embeddingSize = 150

embeddings = tf.Variable(tf.random_uniform([vocabularySize, embeddingSize], -1.0, 1.0))

#set placeholders for training inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[159571, 1])
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

#create dictionary
frame = pd.DataFrame(trainComments)
dictionary = frame.to_dict()

#training the model
feed_dict = {train_inputs: trainComments, train_labels: y}

init = tf.global_variables_initializer()




















