#!/usr/bin/env python3
"""
Write a Python function that returns all
students sorted by average score
"""


def top_students(mongo_collection):
    """
    mongo_collection : collection
    """
    for doc in mongo_collection.find():
        note = [i.score in doc['topics']]
        doc.update_one(
            { 'name' : doc.name },
            {'$set' : { 'averageScore' : sum(note)/len(note) }})
    return mongo_collection.sort("averageScore", -1)
    