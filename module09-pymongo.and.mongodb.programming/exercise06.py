from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
isbankasi = mongo_client['isbankasi']
accounts_collection = isbankasi['accounts']

result = accounts_collection.delete_many(
    {"status": {"$in": ["BLOCKED", "CLOSED"]}}
)

print(f"{result.deleted_count} documents removed!")