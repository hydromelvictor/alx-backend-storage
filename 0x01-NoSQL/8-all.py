#!/usr/bin/env python3
"""
Write a Python function that lists all documents
in a collection
"""


def list_all(mongo_collection):
    """
    mongo_collecion : db.collection
    """
    return mongo_collection.find()
