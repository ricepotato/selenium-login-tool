from flask import Flask, request, jsonify
from browser import login


def create_app():
    app = Flask(__name__)
    route(app)
    return app


def route(app: Flask):
    @app.route("/krav/", methods=["POST"])
    def krav():
        json = request.get_json()
        text = login(json["url"], json["id"], json["password"])
        return jsonify({"text": text})


app = create_app()
