import pytest
import json

from src.chef.sous_chef import SpoonacularSousChef
import test_config as cfg

@pytest.fixture
def sous_chef():
    return SpoonacularSousChef()

def test_get_random_meals(sous_chef):
    # given: 
    desired_number_of_meals = 2

    # when:
    meals = sous_chef.get_random_meals(desired_number_of_meals)

    # then:
    assert len(meals) == desired_number_of_meals

    for meal in meals:
        keys = meal.keys()
        assert "title" in keys
        assert "spoonacularSourceUrl" in keys

        if cfg.VERBOSE:
            print()
            print("### MEAL ###")
            print(f'Title\t: {meal["title"]}')
            print(f'Link\t: {meal["spoonacularSourceUrl"]}')
            print(f'Likes\t: {meal["aggregateLikes"]}')
            print()

    if cfg.DETAILED_VERBOSE:
        pretty = json.dumps(meals, indent=2)
        print(pretty)


def test_get_popular_random_meals(sous_chef):
    # given: 
    desired_number_of_meals = 3

    # when:
    meals = sous_chef.get_popular_random_meals(desired_number_of_meals)

    # then:
    assert len(meals) == desired_number_of_meals

    previous_recipe_likes = meals[0]["aggregateLikes"]

    for meal in meals:
        keys = meal.keys()
        assert "title" in keys
        assert "spoonacularSourceUrl" in keys
        assert meal["aggregateLikes"] <= previous_recipe_likes

        if cfg.VERBOSE:
            print()
            print("### MEAL ###")
            print(f'Title\t: {meal["title"]}')
            print(f'Link\t: {meal["spoonacularSourceUrl"]}')
            print(f'Likes\t: {meal["aggregateLikes"]}')
            print()

    if cfg.DETAILED_VERBOSE:
        pretty = json.dumps(meals, indent=2)
        print(pretty)