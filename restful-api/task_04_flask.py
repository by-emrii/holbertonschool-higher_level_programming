#!/usr/bin/python3
"""
This is the "task_04_flask.py" module.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_username(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def create_user():
    data = request.get_json()  # parse incoming json

    if not data:
        return jsonify({"error": "no input data received"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "user already exists"}), 400

    # add user to dict
    users[username] = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
        }), 201


if __name__ == "__main__":
    app.run()
