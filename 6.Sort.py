import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse

coll = mydb["users"]    # Create collection


# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

# Ascending Order:
# Use the value 1 as the second parameter to sort descending.
doc = coll.find().sort("name")  # By default acsending order, also can write "...sort("name", 1)

for x in doc:
    print(x)

# Descending Order:
# Use the value -1 as the second parameter to sort descending.
doc = coll.find().sort("name", -1)

for x in doc:
    print(x)
