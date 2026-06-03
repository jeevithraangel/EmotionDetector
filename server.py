from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    # ✅ Handle blank input error
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid input! Please enter some text."

    result = emotion_detector(text_to_analyze)

    return (
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"Dominant emotion: {result['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(debug=True)