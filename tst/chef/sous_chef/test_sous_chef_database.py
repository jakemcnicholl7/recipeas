import pytest

from src.chef.sous_chef.database_sous_chef import DatabaseSousChef
from src.database.database import Database

mocked_meals = [
    {
        "title": "Chicken curry so good you might throw up",
        "method": "Put the chicken on a plate",
        "ingredients": "chicken"
    },
    {
        "title": "kebap exchange baby",
        "method": "get drunk and go to a nightclub, grab a kebap on your way home",
        "ingredients": "kebap is secret"
    }
]

@pytest.fixture
def sous_chef(mocker):
    db = Database()
    mocker.patch.object(db, "get_random_items", return_value=mocked_meals)
    return DatabaseSousChef(db)

def test_get_random_meals(sous_chef):
    # when
    meals = sous_chef.get_random_meals(2)

    # then 
    assert mocked_meals == meals

