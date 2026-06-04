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

    try:
        response = requests.post(url, json=body, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

        # correct dominant emotion calculation
        result["dominant_emotion"] = max(
            result,
            key=lambda x: result[x]
        )

        return result

    except Exception as e:
        print("ERROR:", e)
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }