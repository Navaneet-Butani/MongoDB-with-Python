import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mongo_python_demo"]  # Create databse

coll = mydb["users"]    # Create collection

# To limit the result in MongoDB, we use the limit() method.
# The limit() method takes one parameter, a number defining how many documents to return.

result = coll.find().limit(3)

for x in result:
    print(x)
