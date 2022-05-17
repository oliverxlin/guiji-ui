from flask import Flask
from apps.manager import bp as blueprint
from flask_cors import *

app = Flask(__name__)

app.register_blueprint(blueprint)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    print("'Hello World!'")
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post():
    print("Hello World! post")
    return 'Hello World!'

if __name__ == '__main__':
    app.run()