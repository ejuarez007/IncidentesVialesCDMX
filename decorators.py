import os 
from pymongo import MongoClient

host = os.environ['MONGO_HOST']
port = int(os.environ['MONGO_PORT'])

def open_close_connection(func):
    def wrapper(*args, **kwargs):
        # open connection 
        conn = MongoClient(host=host, port=port)
        func(*args, **kwargs, conn=conn)
        conn.close()
    return wrapper
