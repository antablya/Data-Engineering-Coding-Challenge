import pymongo
from flask import Flask
from json import dumps
app = Flask(__name__)


#Connecting to the database
client = pymongo.MongoClient("mongodb+srv://dbUser1:1234@cluster0.hfrlh.mongodb.net/testdb?retryWrites=true&w=majority")
db=client["testdb"]
collection=db["testcollection"]

#Search articles by Keywords.
@app.route('/articles',methods=["GET"])
def get_articles():
    final_results=[]
    results = collection.find({"keywords": {"$all": ["coronavirus"]}})


    for result in results:
        result["_id"]=str(result["_id"])
        final_results.append(result)
    return {"data":final_results}


