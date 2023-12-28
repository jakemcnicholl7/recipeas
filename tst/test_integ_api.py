from flask import Flask, jsonify
from src.api import application
import pytest
import json
from tst.test_helper import database_helper

database_helper.start_recipe_database()

@pytest.fixture
def client():
    with application.test_client() as client:
        yield client

def test_get_random_meals(client):
    response = client.get("/")

    assert 200 == response.status_code

    content = response.get_data().decode('utf-8')

    expected_fields = ["title", "ingredients", "method", "introduction"]

    for field in expected_fields:
        assert field in content

