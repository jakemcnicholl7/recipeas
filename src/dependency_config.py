from src.chef.chef import Chef
from src.chef.sous_chef.sous_chef_spoonacular import SpoonacularSousChef

sous_chef = SpoonacularSousChef()
chef = Chef(sous_chef=sous_chef)

 

