"""
Detect emotions using AI
"""

import requests
import json

def emotion_detector(text_to_analyze):
    """
    This fun detects
    emotion in a text
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)

    
    if response.status_code == 400:
        return {'anger' : None,
                'disgust' : None,
                'fear' : None,
                'joy' : None,
                'sadness' : None,
                'dominant_emotion' : None}
    
    scores = formatted_response['emotionPredictions'][0]['emotion']
    max_value = max(scores.values())
    dominant = [key for key, value in scores.items() if value == max_value]
    scores['dominant_emotion'] = dominant[0]
    return scores
