import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    json_input = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=json_input, headers=headers)

    if response.status_code == 200:
        formatted_response = response.json()

        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        output = {
            "anger": emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness")
        }

        output["dominant_emotion"] = max(output, key=output.get)

        return output

    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }