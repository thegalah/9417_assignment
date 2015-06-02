import os

#load vocabulary
with open ("vocabulary.txt", "r") as myfile:
    vocab=myfile.read().strip().split('\n')


#path to training set
training_set='../20news-bydate/20news-bydate-test/'

#get list of classes
V=os.listdir(training_set)

#fix for macos
V.remove('.DS_Store')

#foreach class V
for v in V:
	#get documents
	docs=os.listdir(training_set+v)
	print(len(docs))