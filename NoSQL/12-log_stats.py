#!/usr/bin/env python3
"""
log module
"""

from pymongo import MongoClient


def log_stats():
    """
    Connects to the MongoDB database and retrieves statistics from the 'nginx' 
    collection of the 'logs' database. It prints the following information:
    
    1. Total number of logs.
    2. Count of logs for each specified HTTP method (GET, POST, PUT, PATCH, DELETE).
    3. Count of status check requests (GET requests to the path '/status').

    Usage:
        Call this function to output log statistics to the console.
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
