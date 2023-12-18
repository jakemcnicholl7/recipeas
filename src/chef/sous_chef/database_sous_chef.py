import pymongo
from src.chef.sous_chef.sous_chef import SousChef

class DatabaseSousChef(SousChef):

    def __init__(self, db):
        self.db = db


    def get_random_meals(self, number=1):
        return self.db.get_random_items(number)
