from pymongo import MongoClient
db = MongoClient('localhost', 27017)
base = db.avito['мужские часы']
base.delete_many({})

# db = mongodb://dess:Sanich523524@46.17.250.22':27017
# client = MongoClient("mongodb://dess:Sanich523524@46.17.250.22:27017")
# db = MongoClient('mongodb://dess:dess@46.17.250.22:27017/')             #'mongodb://dess:dess@46.17.250.22:27017/'

print()


