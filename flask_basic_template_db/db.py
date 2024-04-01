from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()

# db_list = client.list_database_names()
# print(db_list)

manga_db = client.mangadb
manga_collection = manga_db.best_selling_manga

def mangas_list():
    mangas = manga_collection.find()
    return list(mangas)