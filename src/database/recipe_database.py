import pymongo

class RecipeDatabase():

    def __init__(self, config):
        self.config = config
        self.client = pymongo.MongoClient(config["data"]["database_endpoint"]) 
        self.db = self.client[config["data"]["recipeas_database_name"]] 
        self.collection = self.db[config["data"]["recipe_collection_name"]] 


    def get_random_items(self, size=1):
        pipeline = [
            {"$sample": {"size": size}}, 
            {"$project": {"_id": 0}}
        ]  
        return list(self.collection.aggregate(pipeline))


