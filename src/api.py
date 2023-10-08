from flask import Flask, jsonify

from src.dependency_config import chef

application = Flask(__name__)

@application.route('/')
def get_random_meals(chef=chef):
    return chef.make_random_meals()


if __name__ == '__main__':
    application.run()
