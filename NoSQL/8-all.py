#!/usr/bin/env python3

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    return list(mongo_collection.find())
