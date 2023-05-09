"""
Write a Python function that returns the list of
school having a specific topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection : collection
    topic : list
    """
    dbname = []
    for doc in mongo_collection.find({ 'topic' : topic }):
        dbname.append(doc)
    return dbname
