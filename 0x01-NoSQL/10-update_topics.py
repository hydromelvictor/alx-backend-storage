"""
Write a Python function that changes all topics
of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    mongo_collection : collection
    name : str
    topics : list:str
    """
    mongo_collection.update(
        { 'name' : name },
        { '$inc': { 'topics' : topics } }
    )
