import os
import time

import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

class SousChef:
    def __init__(self):
        ...
    
    def get_random_meals(self, number):
        ...


class SpoonacularSousChef(SousChef):
    URL_ENDPOINT = "https://api.spoonacular.com/recipes/"
    HEADERS = {"x-api-key": SPOONACULAR_API_KEY}
    RECIPE_EXPLORATION_FACTOR = 3 
    FIELDS_TO_RETURN = {"title", "aggregateLikes", "spoonacularSourceUrl"}

    def __init__(self):
        ...

    def compose_url(self, path_params, query_params):
        if query_params is None:
            return SpoonacularSousChef.URL_ENDPOINT + "/".join(path_params)
        return SpoonacularSousChef.URL_ENDPOINT + "/".join(path_params) + "?" + urlencode(query_params)

    def get_random_meals(self, number):
        path_params = ["complexSearch"]
        query_params = {   
            "number": str(number), 
            "sort": "random",
            "addRecipeInformation": "true",
            "excludeIngredients": "eggs,cabbage",
            "minProtein": "10",
            "maxSugar": "10"
            }

        path = self.compose_url(path_params, query_params);
        response = requests.get(path, headers=SpoonacularSousChef.HEADERS)
        meals = response.json()["results"]
        return self.simplify_meals(meals)

    def simplify_meals(self, meals):
        simplified_meals = []
        for meal in meals:
            simplified_meal = {}
            for field in SpoonacularSousChef.FIELDS_TO_RETURN:
                if field in meal:
                    simplified_meal[field] = meal[field]
            simplified_meals.append(simplified_meal)
        return simplified_meals


    def get_popular_random_meals(self, number):
        random_meal_pool = self.get_random_meals(number * SpoonacularSousChef.RECIPE_EXPLORATION_FACTOR)

        random_meals_sorted_by_popularity = sorted(random_meal_pool, key=lambda x: x["aggregateLikes"], reverse=True)

        return random_meals_sorted_by_popularity[0:number]

    def get_meal_with_id(self, id):
        path_params = [str(id), "information"]
        path = self.compose_url(path_params, None)
        response = requests.get(path, headers=SpoonacularSousChef.HEADERS)
        return response.json()

