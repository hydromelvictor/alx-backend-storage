"""
Write a Python function that inserts a new document
in a collection based on kwargs
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection : collection
    kwargs : dict
    """
    new = mongo_collection.insert_one(**kwargs)
    return new.inserted_id
