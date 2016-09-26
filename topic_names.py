
with open('/home/joseph/Desktop/Project_Topic_Modelling/topic-keys-news_articles.txt') as input:

   topic_keys_lines = input.readlines()

topic_words = []

for line in topic_keys_lines:
	
   _, _, words = line.split('\t')  
   words = words.rstrip().split(' ')  
   topic_words.append(words)

print(topic_words)

"""
for t in range(len(topic_words)):
   print("Topic {}: {}".format(t, ' '.join(topic_words[t])))
"""