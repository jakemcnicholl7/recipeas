from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def hello_world():
    return jsonify({"Greeting":"Hello World!"})

if __name__ == '__main__':
    application.run()
