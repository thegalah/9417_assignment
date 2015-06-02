import os
import re

#load vocabulary
with open ("vocab", "r") as myfile:
    vocab=set(myfile.read().strip().split('\n'))



#path to training set
training_set='../20news-bydate/20news-bydate-train/'

#get list of classes
V=os.listdir(training_set)

#fix for macos
try:
	V.remove('.DS_Store')
except ValueError:
	pass


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



