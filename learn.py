import os
import re
from math import log

#load vocabulary
with open ("vocab", "r") as myfile:
    vocab=set(myfile.read().strip().split('\n'))
vocab_length=len(vocab)


#path to training set
training_set='../20news-bydate/20news-bydate-train/'
#path to test/validation set
test_set='../20news-bydate/20news-bydate-test/'

#get list of classes
V=os.listdir(training_set)



#count number of training documents
count=0

#generate probabilities for the words in the vocab
learnings=dict();

for v in V:
	count=count+len(os.listdir(training_set+v))
#foreach class V
for v in V:
	#get documents
	docs=os.listdir(training_set+v)

	#P(v_j)
	log_doc_freq=log(len(docs))-log(count)
	text_j='';
	for doc in docs:
		doc_path=training_set+v+'/'+doc
		myfile=open(doc_path,'r')
		file_string=myfile.read()
		text_j=text_j+' '+file_string

	#clean up text
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
TS=os.listdir(test_set)

doc_count=0
correct=0
for cat in TS:
	docs=os.listdir(test_set+cat)
	#classify document
	for doc in docs:
		doc_count+=1
		doc_path=test_set+cat+'/'+doc
		myfile=open(doc_path,'r')
		file_string=myfile.read()
		#clean up text
		#remove non ascii
		file_string=re.sub(r'([^\s\w]|_)+', '', file_string)

		#substitute all whitespace with
		file_string=re.sub( '\s+', ' ', file_string ).strip().lower()
		file_string=file_string.split(' ')
		max_prob=0
		probable_cat='';
		for v in V:
			p=0;
			for word in file_string:
				if word in learnings[v]:
					p+=learnings[v][word]
			if max_prob==0 or max_prob<p:
				max_prob=p
				probable_cat=v

		if probable_cat==cat:
			correct+=1
		print correct,'/',doc_count,'[',((correct/doc_count)*100),'%','correct]'



