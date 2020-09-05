import nltk
nltk.download('punkt')
import pymongo
import newspaper

#Connecting to the database
client = pymongo.MongoClient("mongodb+srv://dbUser1:1234@cluster0.hfrlh.mongodb.net/testdb?retryWrites=true&w=majority")
db=client["testdb"]
collection=db["testcollection"]
#Retrieving data with specified attributes
result = collection.find_one({"title":"Climate change: Power companies 'hindering' move to green energy"})
print(result['title'],result['text'])
