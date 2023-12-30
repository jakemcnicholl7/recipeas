from flask import Flask, jsonify
from flask_cors import CORS

from src.dependency_config import chef

application = Flask(__name__)

# CORS
# Allows the browser running on localhost:3000 to make requests to this backend endpoint 

CORS(application, resources={r"/*": {"origins": "http://localhost:3000"}})

@application.route('/')
def get_random_meals(chef=chef):
    return jsonify(chef.make_random_meals())


if __name__ == '__main__':
    application.run()
