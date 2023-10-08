import pytest
from unittest.mock import Mock

from src.chef.chef import Chef

@pytest.fixture
def sous_chef():
    return Mock()

@pytest.fixture
def chef(sous_chef):
    return Chef(sous_chef)

def test_get_random_meal(chef, sous_chef):
    # Given
    sous_chef.get_random_meals.return_value = "Brocolli";

    # When
    meal = chef.make_random_meals()

    # Then
    assert meal == "Brocolli"

