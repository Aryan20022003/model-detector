from flask import Flask, request, jsonify

from main.tasks import (
    backgroundCat,
    backgroundBitCoin,
    liveStreamDetection,
    staticMediaDetection,
)


app = Flask(__name__)



@app.route("/", methods=["GET"])
def test():
    return jsonify({"status": 200, "message": "It works!"})


@app.route("/cat", methods=["GET"])
def cat():
    print("cat one")
    backgroundCat.delay()
    return jsonify({"status": 200, "message": "Cat is coming!"})


@app.route("/bitcoin", methods=["GET"])
def bitcoin():
    print("bitcoin one")
    backgroundBitCoin.delay()
    return jsonify({"status": 200, "message": "Bitcoin is coming!"})


# will convert it to post and will get the image Id from user
@app.route("/staticAnalysis", methods=["GET", "POST"])
def staticAnalysis():
    print("staticAnalysis one")
    # imageId=request.json['date']['imageId']
    staticMediaDetection.delay()
    return jsonify({"status": 200, "message": "staticAnalysis is coming!"})


@app.route("/liveStreamAnalysis", methods=["GET", "POST"])
def liveStreamAnalysis():
    print("liveStreamAnalysis one")
    # streamId=request.json['date']['streamId']
    liveStreamDetection.delay()
    return jsonify({"status": 200, "message": "liveStreamAnalysis is coming!"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
