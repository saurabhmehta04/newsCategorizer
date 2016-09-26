
import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client['news']
res=db.articles.find({},{'_id':0,'text':1,'id':1})

			

for r in res:
	try:
		f=open("text/"+str(r['id']),"wb")
		f.write(r['text'].encode('utf8'))
		f.close()
	except:
		continue

	