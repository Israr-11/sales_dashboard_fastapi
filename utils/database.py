from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

def dBConnection():
    try:
        load_dotenv()
        mongo_url = os.getenv("MONGO_URI")
        db_name = os.getenv("DB_NAME")
        collection_name = os.getenv("COLLECTION_NAME")

        client = MongoClient(mongo_url, server_api=ServerApi('1'))
        db = client[db_name]
        collection = db[collection_name]

        # Check if the connection is successful or not
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client, db, collection
    except Exception as e:
        print("Failed to connect to MongoDB:", e)
