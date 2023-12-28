import pytest

from src.database.recipe_database import RecipeDatabase
from src import config
from tst.test_helper import database_helper

database_helper.start_recipe_database()

@pytest.fixture
def recipe_database():
    configuration = config.load()
    return RecipeDatabase(configuration)

def test_get_random_items(recipe_database):
    # given:
    no_items = 3
    expected_fields = ["title", "ingredients", "method", "introduction"]

    # when:
    items = recipe_database.get_random_items(no_items)

    for item in items:
        item_fields = item.keys()
        for field in expected_fields:
            assert field in item_fields


