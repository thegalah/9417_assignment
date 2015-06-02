import os

#path to training set
training_set='../20news-bydate/20news-bydate-test/'

#get list of classes
V=os.listdir(training_set)

print(V)