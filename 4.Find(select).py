import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mongo_python_demo"]
coll = mydb["users"]


#--------- Find One ----------#
# The find_one() method returns the first occurrence in the selection.
x = coll.find_one()
print(x)


#---------- Find Many ----------#
# The find() method returns all occurrences in the selection.
# No parameters in the find() method gives you the same result as SELECT * in MySQL.
for x in coll.find():
    print(x)    

# The second parameter of the find() method is an object describing which fields to include in the result.
# In 2nd parenthesis of the find argument assign 1 to whom you want to select and other will automatically assigned to 0.
# In 2nd parenthesis of the find argument assign 0 to whom you don't want to select and other will automatically assigned to 1.
# Value 0 and 1 to the field name can't be applied together in the parenthesis except "_id", you can assign 0 to "_id" while assigning 1 to other.
for x in coll.find({}, {"_id":0, "name":1}):
    print(x)