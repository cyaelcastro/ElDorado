from crypt import methods
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello():
    return "Hello World from Docker!"


@app.route('/print', methods=["POST"])
def print_content():
    data = request.args.get("content")
    return f"Received content: {data}"
