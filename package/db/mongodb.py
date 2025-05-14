from pymongo import MongoClient

from package.db.configdb import Config

mongo_client = None
db = None


# Initialize the MongoDB client and database
def init_db():
    global mongo_client, db
    if mongo_client is None:
        mongo_client = MongoClient(Config.MONGO_URI)
        db = mongo_client[Config.DB_NAME]
        print("MongoDB client initialized.")
    else:
        print("MongoDB client already initialized.")
        # print("MongoDB client already initialized.")


def get_db():
    if db is None:
        raise Exception("Database not initialized. Call init_db() first.")
    return db
