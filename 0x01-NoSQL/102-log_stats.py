#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10
of the most present IPs in the collection nginx
of the database logs
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
          ".format(collection.count_doucments(),
          collection.count_documents({ 'method' : 'GET' }),
          collection.count_documents({ 'method' : 'POST' }),
          collection.count_documents({ 'method' : 'PUT' }),
          collection.count_documents({ 'method' : 'PATCH' }),
          collection.count_documents({ 'method' : 'DELETE' }),
          collection.count_documents({ 'method' : 'GET', 'path' : '/status' })
          ))
    print("IPs:")
    dix = collection.find().sort("IP", -1).limit(10)
    for i in dix:
        print("\t{}".format(i.IP))
