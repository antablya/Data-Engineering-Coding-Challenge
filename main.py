import nltk
nltk.download('punkt')
import pymongo
import newspaper

#Creating Newspaper from bbc
cnn_paper = newspaper.build('http://bbc.com',memoize_articles=False)

#Connecting to the MongoDB
client = pymongo.MongoClient("mongodb+srv://dbUser1:1234@cluster0.hfrlh.mongodb.net/testdb?retryWrites=true&w=majority")
db=client["testdb"]
collection=db["testcollection"]

#Adding articles to the database
unique_articles=[]
for article in cnn_paper.articles:

     try:
         article.download()
         article.parse()
         article.nlp()
     except Exception as e:
         print(e)
         continue
     else:
         if article.title not in unique_articles and any(char.isdigit() for char in article.url):
            post={"title":article.title,"url":article.url,"author":article.authors,"keywords": article.keywords,"text":article.text}
            collection.insert_one(post)
            unique_articles.append(article.title)


