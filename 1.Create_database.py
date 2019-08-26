import pymongo

# To create a database in MongoDB, start by creating a MongoClient object
client = pymongo.MongoClient("mongodb://localhost:27017/")


# Specifing Database "mongo_python_demo"
mydb = client["mongo_python_demo"]

# In MongoDB, a database is not created until it gets content, 
# so if this is your first time creating a database, 
# you should complete the next create collection and create document then check for database is created or not!


# Return a list of your system's databases
print(client.list_database_names())