import os
import codecs
import re

#load vocabulary
with open ("vocabulary.txt", "r") as myfile:
    vocab=myfile.read().strip().split('\n')


#path to training set
training_set='../20news-bydate/20news-bydate-train/'

#get list of classes
V=os.listdir(training_set)

#fix for macos
try:
	V.remove('.DS_Store')
except ValueError:
	pass

#count number of training documents
count=0
for v in V:
	count=count+len(os.listdir(training_set+v))

#foreach class V
for v in V:
	#get documents
	docs=os.listdir(training_set+v)
	#fix for macos
	try:
		docs.remove('.DS_Store')
	except ValueError:
		pass
	#P(v_j)
	probability_vj=len(docs)/count
	text_j='';
	for doc in docs:
		doc_path=training_set+v+'/'+doc
		myfile=open(doc_path,'r')
		file_string=myfile.read()
		text_j=text_j+' '+file_string

	text_j=re.sub(r'([^\s\w]|_)+', '', text_j)
	print text_j
