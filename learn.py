import os
import re
from math import log

#load vocabulary
with open ("vocab", "r") as myfile:
    vocab=set(myfile.read().strip().split('\n'))
vocab_length=len(vocab)


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
	document_frequency=len(docs)/count
	text_j='';
	for doc in docs:
		doc_path=training_set+v+'/'+doc
		myfile=open(doc_path,'r')
		file_string=myfile.read()
		text_j=text_j+' '+file_string

	#remove non ascii
	text_j=re.sub(r'([^\s\w]|_)+', '', text_j)

	#substitute all whitespace with
	text_j=re.sub( '\s+', ' ', text_j ).strip().lower()
	text_j=text_j.split(' ')
	#number of text positions or length
	n=len(text_j)
	print n
	occurences=dict()
	for word in text_j:
		if word in occurences:
			occurences[word]+=1
		else:
			occurences[word]=1
	
	probabilities=dict()

	for word in vocab:
		if word in occurences:
			log_prob=log(occurences[word]+1/vocab_length)
		else:
			log_prob=log(1/vocab_length)

		log_prob+=log(document_frequency)
		probabilities[word]=log_prob
		print log_prob


