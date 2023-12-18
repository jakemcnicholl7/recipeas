import pymongo
import pandas as pd
import sys
import os

from src import config

CONFIGURATION = config.load()

MONGO_ENDPOINT = CONFIGURATION["data"]["database_endpoint"] 
RECIPEAS_DATABASE = CONFIGURATION["data"]["recipes_database_name"] 
RECIPE_COLLECTION = CONFIGURATION["data"]["recipes_collection_name"] 
RECIPE_DB_SOURCE_FILE = "data/recipes.csv"

RESET = False


def main():
    setup_recipe_db()


def setup_recipe_db():
    if not os.path.exists(RECIPE_DB_SOURCE_FILE):
        print("[ERROR] No database source file exists")
        sys.exit(1)

    client = pymongo.MongoClient(MONGO_ENDPOINT) 
    
    db = client[RECIPEAS_DATABASE]

    if RESET:
        reset_db(db)

    if is_db_already_setup(db):
        print("[INFO] Database is already set up")
        sys.exit(0)

    insert_data(db)


def reset_db(db):
    collection = db[RECIPE_COLLECTION]
    collection.drop()
        
        
def insert_data(db):
    collection = db[RECIPE_COLLECTION]

    source_db = pd.read_csv(RECIPE_DB_SOURCE_FILE)
    source_data = source_db.to_dict(orient="records")
    total_data = len(source_data)

    index = 0
    insert_size = 5

    while index < total_data:
        insert_start = index
        insert_end = min(index + insert_size, total_data)
        
        data_insert = source_data[insert_start: insert_end]
        collection.insert_many(data_insert)

        index = insert_end


def is_db_already_setup(db):
    return RECIPE_COLLECTION in db.list_collection_names()


if __name__ == "__main__":
    main()

