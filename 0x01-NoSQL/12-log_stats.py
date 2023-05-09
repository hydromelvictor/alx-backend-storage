#!/usr/bin/env python3
"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB
"""
if __name__ == '__main__':
      from pymongo import MongoClient


      client = MongoClient('mongodb://127.0.0.1:27017')
      db = client.logs
      collection = db.ngnix

      print("{} logs\n\
            Methods:\n\
            \tmethods GET: {}\n\
            \tmethods POST: {}\n\
            \tmethods PUT: {}\n\
            \tmethods PATCH: {}\n\
            \tmethods DELETE: {}\n\
            {} status check\
            ".format(collection.count_documents(),
            collection.count_documents({ 'method' : 'GET' }),
            collection.count_documents({ 'method' : 'POST' }),
            collection.count_documents({ 'method' : 'PUT' }),
            collection.count_documents({ 'method' : 'PATCH' }),
            collection.count_documents({ 'method' : 'DELETE' }),
            collection.count_documents({ 'method' : 'GET', 'path' : '/status' })
            ))
