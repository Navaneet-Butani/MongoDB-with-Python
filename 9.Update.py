import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse

coll = mydb["users"]    # Create collection


#------------- Update One --------------#

# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# The first parameter of the update_one() method is a query object defining which document to update.
# If the query finds more than one record, only the first occurrence is updated.
# The second parameter is an object defining the new values of the document.

query = {"name" : "Rakesh"}

newquery = {"$set" : {"city" : "Gandhinagar"}}

coll.update_one(query, newquery)

for x in coll.find():
    print(x)



#------------- Update Many ------------#
# To update all documents that meets the criteria of the query, use the update_many() method.

# Update all documents where the city starts with the letter "S"

query = {"city" : {"$regex" : "^S"}}

newquery = {"$set" : {"city" : "Delhi"}}

x = coll.update_many(query, newquery)

print(x.modified_count, "documents updated.")   # WIll give you count of modified field
