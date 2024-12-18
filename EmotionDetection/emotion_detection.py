import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    text_response = json.loads(response.text)

    if response.status_code == 200:
        # Extraire les scores d'émotions
        emotion_scores = text_response['emotionPredictions'][0]['emotion']
        # Identifier l'émotion dominante
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        formatted_response = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
        }
    # If the response status code is 400, empty dico
    elif response.status_code == 400:
        formatted_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    

    return formatted_response
