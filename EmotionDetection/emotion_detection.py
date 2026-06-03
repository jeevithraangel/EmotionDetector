import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    body = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    data = response.json()

    emotions = data["emotionPredictions"][0]["emotion"]

    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    result["dominant_emotion"] = max(result, key=result.get)

    return result