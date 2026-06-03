def emotion_detector(text):
    text = text.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    joy_words = ["happy", "joy", "good", "great", "excellent"]
    sad_words = ["sad", "cry", "bad", "unhappy"]
    anger_words = ["angry", "mad", "hate"]
    fear_words = ["fear", "scared", "danger"]
    disgust_words = ["disgust", "gross"]

    words = text.split()

    for w in words:
        if w in joy_words:
            emotions["joy"] += 1
        if w in sad_words:
            emotions["sadness"] += 1
        if w in anger_words:
            emotions["anger"] += 1
        if w in fear_words:
            emotions["fear"] += 1
        if w in disgust_words:
            emotions["disgust"] += 1

    dominant = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant
    return emotions