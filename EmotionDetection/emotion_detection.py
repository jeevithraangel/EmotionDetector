def emotion_detector(text):
    text = text.lower()

    emotions = {
        "joy": 0,
        "sadness": 0,
        "anger": 0,
        "fear": 0,
        "disgust": 0,
        "surprise": 0,
        "love": 0,
        "neutral": 0
    }

    joy_words = ["happy", "joy", "great", "excellent", "wonderful", "good", "amazing"]
    sadness_words = ["sad", "cry", "depressed", "lonely", "unhappy"]
    anger_words = ["angry", "mad", "hate", "furious", "annoyed"]
    fear_words = ["fear", "afraid", "scared", "danger", "panic", "worried"]
    disgust_words = ["disgust", "gross", "dirty", "nasty", "horrible"]
    surprise_words = ["surprised", "wow", "shocked", "unexpected"]
    love_words = ["love", "like", "adore", "care", "affection"]

    words = text.split()

    matched = False

    for word in words:

        if word in joy_words:
            emotions["joy"] += 1
            matched = True

        if word in sadness_words:
            emotions["sadness"] += 1
            matched = True

        if word in anger_words:
            emotions["anger"] += 1
            matched = True

        if word in fear_words:
            emotions["fear"] += 1
            matched = True

        if word in disgust_words:
            emotions["disgust"] += 1
            matched = True

        if word in surprise_words:
            emotions["surprise"] += 1
            matched = True

        if word in love_words:
            emotions["love"] += 1
            matched = True

    if not matched:
        emotions["neutral"] = 1

    max_score = max(emotions.values())

    if max_score == 0:
        emotions["dominant_emotion"] = "neutral"
    else:
        top = [k for k, v in emotions.items() if v == max_score]

        emotions["dominant_emotion"] = top[0] if len(top) == 1 else "tie: " + ", ".join(top)

    return emotions
    text = text.lower()

    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    joy_words = [
        "happy", "joy", "love", "great",
        "excellent", "wonderful", "excited",
        "amazing", "fantastic", "good"
    ]

    sad_words = [
        "sad", "cry", "upset",
        "depressed", "unhappy",
        "lonely", "heartbroken"
    ]

    anger_words = [
        "angry", "mad", "hate",
        "furious", "annoyed",
        "irritated", "rage"
    ]

    fear_words = [
        "fear", "afraid", "scared",
        "danger", "terror", "panic",
        "worried", "nervous", "anxious"
    ]

    disgust_words = [
        "disgust", "gross",
        "awful", "nasty",
        "horrible", "dirty"
    ]

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

    max_score = max(emotions.values())

    if max_score == 0:
        emotions["dominant_emotion"] = "No emotion detected"
    else:
        top_emotions = [
            emotion
            for emotion, score in emotions.items()
            if score == max_score
        ]

        if len(top_emotions) == 1:
            emotions["dominant_emotion"] = top_emotions[0]
        else:
            emotions["dominant_emotion"] = "Tie: " + ", ".join(top_emotions)

    return emotions