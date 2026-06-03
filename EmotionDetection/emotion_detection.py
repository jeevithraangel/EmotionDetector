def emotion_detector(text):
    text = text.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    joy_words = ["happy", "joy", "good", "great", "excellent", "love"]
    sad_words = ["sad", "cry", "unhappy", "bad"]
    anger_words = ["angry", "mad", "hate"]
    fear_words = ["fear", "scared", "danger", "worried"]
    disgust_words = ["disgust", "gross", "dirty"]

    words = text.split()

    for word in words:
        if word in joy_words:
            emotions["joy"] += 1
        if word in sad_words:
            emotions["sadness"] += 1
        if word in anger_words:
            emotions["anger"] += 1
        if word in fear_words:
            emotions["fear"] += 1
        if word in disgust_words:
            emotions["disgust"] += 1

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted output
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }