from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/api/todo/", methods=["POST", "GET"])
def todo():
    if request.method == "GET":
        data = request.json
        with open("task.json", "r") as reader:
            data = json.load(reader)
            # print(data)
            # print("hello")
            return jsonify(data), 200
    return "<h1>Bad request</h1>", 400


@app.route("/api/update/", methods=["POST", "GET"])
def update():
    if request.method == "POST":
        data = request.json
        # print(data)

        with open("task.json", "w") as writer:
            json.dump(data, writer)

    return "<h1>Updated</h1>", 200


if __name__ == "__main__":
    app.run()
