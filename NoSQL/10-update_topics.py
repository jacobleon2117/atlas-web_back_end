#!/usr/bin/env python3

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on keyword arguments.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
