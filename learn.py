import os
import re
from math import log

# get dir without hidden directories
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


#load vocabulary
with open ("vocab", "r") as myfile:
    vocab=set(myfile.read().strip().split('\n'))
vocab_length=len(vocab)


#path to training set
training_set='../20news-bydate/20news-bydate-train/'
#path to test/validation set
test_set='../20news-bydate/20news-bydate-test/'

#get list of classes
V=os.listdir_nohidden(training_set)


#count number of training documents
count=0

#generate probabilities for the words in the vocab
learnings=dict();

for v in V:
	count=count+len(os.listdir(training_set+v))
#foreach class V
for v in V:
	#get documents
	docs=os.listdir_nohidden(training_set+v)
	#P(v_j)
	log_doc_freq=log(len(docs))-log(count)
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
	print 'learning['+str(n)+']:'+v
	occurences=dict()
	for word in text_j:
		if word in occurences:
			occurences[word]+=1
		else:
			occurences[word]=1
	
	probabilities=dict()

	for word in vocab:
		if word in occurences:
			log_prob=log(occurences[word]+1)-log(len(occurences)+vocab_length)
		else:
			log_prob=-log(len(occurences)+vocab_length)
		log_prob+=log_doc_freq
		probabilities[word]=log_prob

	#insert probabilities into learnings
	learnings[v]=probabilities

#classify test set

#get test sets
TS=os.listdir_nohidden(test_set)


print TS
