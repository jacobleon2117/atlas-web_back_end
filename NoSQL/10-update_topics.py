#!/usr/bin/env python3
"""
    update module
"""

from pymongo import MongoClient


def update_topics(mongo_collection, topic, name):
    """
    Updates the topics of a school in a MongoDB collection.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topic": topic}}
    )
