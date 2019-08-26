import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse

coll = mydb["users"]    # Create collection


#----------- Simple Query ------------#

# The first argument of the find() method is a query object, and is used to limit the search.
query = {"name" : "Rakesh"}

doc = coll.find(query)
for x in doc:
    print(x)    # Will print the result which matches to the query.



#----------- Advance Query -----------#

# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "name" field starts with the letter "M" or higher (alphabetically), use the greater than modifier: {"$gt": "M"}
query = {"name" : { "$gt" : "M" }}

doc = coll.find(query)
for x in doc:
    print(x)    # Will print the results in which name is started with "M" or higher alphabetic.



#------------ Filter With Regular Expressions -------------#

# You can also use regular expressions as a modifier.
# To find only the documents where the "name" field starts with the letter "R", use the regular expression {"$regex": "^R"}
query = {"name" : {"$regex" : "^R"}}

doc = coll.find(query)
for x in doc:
    print(x)    # Will print the results in which name is started with "R" alphabet.
