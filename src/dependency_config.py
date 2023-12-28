from src.chef.chef import Chef
from src.chef.sous_chef.spoonacular_sous_chef import SpoonacularSousChef
from src.chef.sous_chef.database_sous_chef import DatabaseSousChef
from src import config
from src.database.recipe_database import RecipeDatabase


configuration = config.load()


recipe_database = RecipeDatabase(configuration)
sous_chef = DatabaseSousChef(recipe_database)
chef = Chef(sous_chef=sous_chef)

 

