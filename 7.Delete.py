import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse


# For deleting in collection, let's first create one other collection

coll = mydb["Message"]  # Create collection

#---------- Create collection--------#
   


mydict = [
    {"name" : "Rakesh", "message" : "Nice to meet you!"},
    {"name" : "Ricky", "message" : "Hello, how are you?"},
    {"name" : "Joe", "message" : "Good morning, have a nice day!"},
    {"name" : "Jam Paul", "message" : "Happy Birthday to you!"}
    ]

x = coll.insert_many(mydict)

print(x.inserted_ids)    # Will print inserted id


#--------- Delete one document ---------#

# For deleting single documents, delete_one() is used.
# Deleting specific focument which follows the query.
# If there are multiple matches then it will delete 1st occurence.
query = {"name" : "Joe"}

coll.delete_one(query)



#----------- Delete many documents ------------#

# For deleting multiple documents, delete_many() is used.
# Deleting with the all name starting with the "J".
query = {"name" : {"$regex" : "^Ri"}}

x = coll.delete_many(query)
print(str(x.deleted_count)+" records deleted!")





#---------- Delete All Documents in a Collection ------------#

# To delete all documents in a collection, pass an empty query object to the delete_many() method
x = coll.delete_many({})
print(x.deleted_count," records deleted!")
