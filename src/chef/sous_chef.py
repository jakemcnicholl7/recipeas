import os
import time

import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

class SousChef:
    def __init__(self):
        ...
    
    def get_random_meal():
        ...


class SpoonacularSousChef(SousChef):
    URL_ENDPOINT = "https://api.spoonacular.com/recipes/"
    HEADERS = {"x-api-key": SPOONACULAR_API_KEY}

    def __init__(self):
        ...

    def compose_url(self, path_params, query_params):
        if query_params is None:
            return SpoonacularSousChef.URL_ENDPOINT + "/".join(path_params)
        return SpoonacularSousChef.URL_ENDPOINT + "/".join(path_params) + "?" + urlencode(query_params)

    def get_random_meal(self, number=1):
        recipe_id = self.get_random_meal_ids(number);
        time.sleep(0.1)
        recipe = self.get_meal_with_id(recipe_id)
        return recipe


    def get_random_meal_ids(self, number):
        path_params = ["complexSearch"]
        query_params = {   
            "number": "1", 
            "sort": "random"
            }

        path = self.compose_url(path_params, None);
        response = requests.get(path, headers=SpoonacularSousChef.HEADERS)
        return response.json()["results"][0]["id"];


    def get_meal_with_id(self, id):
        path_params = [str(id), "information"]
        path = self.compose_url(path_params, None)
        response = requests.get(path, headers=SpoonacularSousChef.HEADERS)
        return response.json()

