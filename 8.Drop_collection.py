import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse


coll = mydb["Message"] 

# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
coll.drop()
