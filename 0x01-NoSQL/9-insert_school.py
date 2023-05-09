#!/usr/bin/env python3
"""
Write a Python function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection : collection
    kwargs : dict
    """
    new = mongo_collection.insert(kwargs)
    return new.inserted_id
