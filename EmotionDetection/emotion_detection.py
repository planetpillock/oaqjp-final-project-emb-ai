import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    json_data = {"raw_document": {"text": str(text_to_analyze) } }
    response = requests.post(URL, json=json_data, headers=HEADERS)

    if response.status_code == 200:
        data = json.loads(response.text)

        dominant_emotion_value = 0
        dominant_emotion = ""

        emotions = data['emotionPredictions'][0]['emotion']
        for emotion in emotions:
            if emotions[emotion] > dominant_emotion_value:
                dominant_emotion_value = emotions[emotion]
                dominant_emotion = emotion

        emotions['dominant_emotion'] = dominant_emotion
        return emotions

    else:
        return f"Something went wrong: {response.text}" 
        
