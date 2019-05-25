import pymongo as mongo

client = mongo.MongoClient('mongodb://localhost:27017/')
db=client["AlmacenDB"]

coleccionMateriales=db["Materiales"]

list=db.list_collection_names()

if "Materiales" in list:
    print("si, puta")
else:
    print("no, puta")