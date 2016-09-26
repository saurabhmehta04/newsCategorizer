import re
import json
import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client["news"]

topic_docs  = db["topic_docs"]

with open('/home/joseph/Desktop/Project_Topic_Modelling/topic-keys-news_articles.txt') as input:

   topic_keys_lines = input.readlines()

topic_words = []

for line in topic_keys_lines:
	
   _, _, words = line.split('\t')  
   words = words.rstrip().split(' ')  
   topic_words.append(words)

with open("/home/joseph/Desktop/Project_Topic_Modelling/doc-topics-news_articles.txt") as f:

	f.readline()
	topic_doc={}

	for line in f:
		
			l=re.split(r'\t',line)
			doc=int(re.split(r'/',l[1])[-1])
			topic=l[2]
			if topic in topic_doc:topic_doc[topic].append(doc)
			else:topic_doc[topic]=[doc]

	bulk_data=[]
	for topic in topic_doc:
		d={}
		d["labels"]=topic_words[int(topic)]
		d["topic_num"]=topic
		d["docs"]=topic_doc[topic]
		bulk_data.append(d)

	topic_docs.insert(bulk_data)