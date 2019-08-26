import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]

# Craeting collection
coll = mydb["users"]

# MongoDB waits until you have inserted a document before it actually creates the collection.


# Return a list of all collections in your database
print(mydb.list_collection_names())