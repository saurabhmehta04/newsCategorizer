import numpy as np
import itertools
import operator
import os
import glob
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

file_count=len(glob.glob('/home/joseph/Desktop/Project_Topic_Modelling/text/*'))

filenames=["text/"+ str(i) for i in range(1,file_count+1)]
 
def grouper(n, iterable, fillvalue=None):

   "Collect data into fixed-length chunks or blocks"
   args = [iter(iterable)] * n
   return itertools.zip_longest(*args, fillvalue=fillvalue)


doctopic_triples = []
mallet_docnames =  []

with open("/home/joseph/Desktop/Project_Topic_Modelling/doc-topics-news_articles.txt") as f:

   f.readline()

   for line in f:

      docnum, docname, *values = line.rstrip().split('\t')
      mallet_docnames.append(docname)
      

      for topic, share in grouper(2, values):

         triple = (docname, int(topic), float(share))
         doctopic_triples.append(triple)


doctopic_triples = sorted(doctopic_triples, key=operator.itemgetter(0,1))
mallet_docnames = sorted(mallet_docnames)
num_docs = len(mallet_docnames)
num_topics = len(doctopic_triples) // len(mallet_docnames)
doctopic = np.zeros((num_docs, num_topics))

for triple in doctopic_triples:

   docname, topic, share = triple
   row_num = mallet_docnames.index(docname)
   doctopic[row_num, topic] = share


doctopic = np.zeros((num_docs, num_topics))

for i, (doc_name, triples) in enumerate(itertools.groupby(doctopic_triples, key=operator.itemgetter(0))):
   doctopic[i, :] = np.array([share for _, _, share in triples])


article_names = []

for fn in filenames:
   basename = os.path.basename(fn)
   name, ext = os.path.splitext(basename)
   article_names.append(name)

article_names = np.asarray(article_names)
num_groups = len(set(article_names))

#print(article_names)
doctopic_grouped = np.zeros((num_groups, num_topics))

for i, name in enumerate(sorted(set(article_names))):
   doctopic_grouped[i, :] = np.mean(doctopic[article_names == name, :], axis=0)


doctopic = doctopic_grouped

"""
rank=[]

for scores in doctopic[:20]:
   rank.append(np.argmax(scores))

print(rank)


for scores in doctopic:
   #rank.append(scores))
   rank.append(np.argmax(scores))
  

for i,topic in enumerate(rank):
   if topic==27:
      print(i),

categorized_news={}



for i,topic in enumerate(rank):
      if topic in categorized_news: categorized_news[topic].append(i)
      else :  categorized_news[topic]=[i]

print(categorized_news)
"""

with open('/home/joseph/Desktop/Project_Topic_Modelling/topic-keys-news_articles.txt') as input:

   topic_keys_lines = input.readlines()

topic_words = []

for line in topic_keys_lines:

   _, _, words = line.split('\t')  
   words = words.rstrip().split(' ')  
   topic_words.append(words)

for t in range(len(topic_words)):
   print("Topic {}: {}".format(t, ' '.join(topic_words[t])))
