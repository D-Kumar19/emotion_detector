"""
Module to detect emotions in a text

Returns:
    dict: Returns a dictionary with the emotions detected in the text
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects the emotions in the text

    Args:
        text_to_analyze (string): Text to analyze

    Returns:
        dict: Returns a dictionary with the emotions detected in the text
    """

    domain = 'sn-watson-emotion.labs.skills.network'
    url = f'https://{domain}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=header, timeout=10)
    status_code = response.status_code

    emotions = {}

    if status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = get_dominate_emotion(emotions)
    elif status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None
    return emotions


def get_dominate_emotion(emotions):
    """
    Returns the dominant emotion from the emotions dictionary

    Args:
        emotions (dict): emotions dictionary

    Returns:
        string: dominant emotion
    """

    return max(emotions, key=emotions.get)
