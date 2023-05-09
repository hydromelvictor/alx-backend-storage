"""
Write a Python function that lists all documents
in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    mongo_collecion : db.collection
    """
    dbname = []
    for doc in mongo_collection.find():
        dbname.append(doc)
    return dbname
