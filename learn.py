import os

#load vocabulary
with open ("vocabulary.txt", "r") as myfile:
    vocab=myfile.read().strip().split('\n')


#path to training set
training_set='../20news-bydate/20news-bydate-test/'

#get list of classes
V=os.listdir(training_set)

#foreach class V