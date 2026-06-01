from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if not text:
        return jsonify({"error": "Please enter text"})

    result = emotion_detector(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)