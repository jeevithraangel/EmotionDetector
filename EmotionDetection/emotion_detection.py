def emotion_detector(text):

    text = text.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    if any(word in text for word in ["happy", "good", "great", "love"]):
        emotions["joy"] = 1

    if any(word in text for word in ["sad", "lonely", "unhappy"]):
        emotions["sadness"] = 1

    if any(word in text for word in ["angry", "mad", "hate"]):
        emotions["anger"] = 1

    if any(word in text for word in ["fear", "scared", "danger"]):
        emotions["fear"] = 1

    if any(word in text for word in ["disgust", "gross", "dirty"]):
        emotions["disgust"] = 1

    max_value = max(emotions.values())

    if max_value == 0:
        emotions["dominant_emotion"] = "neutral"
    else:
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)

    return {
    "anger": emotions["anger"],
    "disgust": emotions["disgust"],
    "fear": emotions["fear"],
    "joy": emotions["joy"],
    "sadness": emotions["sadness"],
    "dominant_emotion": emotions["dominant_emotion"]
}