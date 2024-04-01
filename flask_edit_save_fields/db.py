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

def get_manga_by_id(mid):
    manga_detail = manga_collection.find_one({"_id": ObjectId(mid)})
    return manga_detail

def update_manga_detail(mid, manda_detail):
    manga_collection.update_one({"_id":ObjectId(mid)},{"$set": manda_detail})
    