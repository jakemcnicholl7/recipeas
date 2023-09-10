import pytest
from src.chef.sous_chef import SpoonacularSousChef

@pytest.fixture
def sous_chef():
    return SpoonacularSousChef()

def test_get_random_meal(sous_chef):
    meal = sous_chef.get_random_meal()
    print(meal["spoonacularSourceUrl"])
    print(meal.keys())
