#!/usr/bin/env python3
"""
Write a Python function that returns all
students sorted by average score
"""


def top_students(mongo_collection):
    """
    mongo_collection : collection
    """
    return mongo_collection.aggregate([
        {
            '$group': {
                'name' : '$name',
                'averageScore' : {'$sum' : '$topics.score'}
            }
        },
        {'$sort' : { 'averageScore' : -1 }}
    ])
    