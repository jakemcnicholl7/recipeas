# Meal Planning API's

### Setup
1. Ensure [pipenv](https://pipenv.pypa.io/en/latest/) is installed on your machine

1. Setup your pthon virtual envirionment:
    `pipenv sync`
1. Run the virtual environment:
    `pipenv shell`

### Runnning

1. Run the API server:
   `python -m src.api`
1. Navigate to http://127.0.0.1:5000 and make a request. 

### Testing

#### All Tests
1. Run
   `pytest`
   or
   `pytest -s` to include printouts
   or
   `pytest tst/chef/test_integ_sous_chef.py::test_get_popular_random_meals` to run a specific test

#### Unit Tests

1. Run
   `pytest -k 'test and not test_integ'`

#### Integration Tests

1. Run
    `pytest -k 'test_integ'`