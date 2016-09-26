# -*- coding: utf-8 -*-
 
import json
import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client['news']



def db_query(topic_id):

	response={}
	topic_doc=db.topic_docs.find_one({'topic_num':str(topic_id)},{'_id':0})
	docs=topic_doc["docs"]
	

	articles=[]

	for doc in docs:

		try:
			article=db.articles.find_one({'id':doc},{'_id':0})
			article["title"]=article["title"].replace("\"","'").replace("\\","")
			article["text"]=article["text"].replace("\"","'").replace("\\","")
			articles.append(article)

		except:

			continue
		

	response["articles"]=articles
	response["labels"]=topic_doc["labels"]
	response["id"]=topic_id

	return json.dumps(response).decode('unicode_escape').encode('ascii','ignore')



	
