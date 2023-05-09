"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB
"""
if __name__ == '__main__':
      from pymongo import MongoClient


      client = MongoClient('mongodb://127.0.0.1:27017')
      db = client.logs
      collection = db.ngnix.find()

      print("{} logs\n\
            Methods:\n\
            \tmethods GET: {}\n\
            \tmethods POST: {}\n\
            \tmethods PUT: {}\n\
            \tmethods PATCH: {}\n\
            \tmethods DELETE: {}\n\
            {} status check\
            ".format(collection.count(),
            collection.find({ 'methods' : 'GET' }).count(),
            collection.find({ 'methods' : 'POST' }).count(),
            collection.find({ 'methods' : 'PUT' }).count(),
            collection.find({ 'methods' : 'PATCH' }).count(),
            collection.find({ 'methods' : 'DELETE' }).count(),
            collection.find({ 'methods' : 'GET', 'path' : '/status' }).count()
            ))
