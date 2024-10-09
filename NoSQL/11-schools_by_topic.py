#!/usr/bin/env python3
"""
    topic module
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic in their topics field.
    """
    return list(mongo_collection.find({"topics": topic}))
