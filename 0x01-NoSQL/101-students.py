"""
Write a Python function that returns all
students sorted by average score
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    mongo_collection : collection
    """
    for doc in mongo_collection.find():
        note = [i.score in doc['topics']]
        doc.update_one(
            { 'name' : doc.name },
            {'$set' : { 'averageScore' : sum(note)/len(note) }})
    dbname = [doc for doc in mongo_collection.sort("averageScore", -1)]
    return dbname
    