import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    formatted_response = json.loads(response.text)
    return formatted_response

def emotion_predictor(detected_text):
    emotions = detected_text['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    max_emotion = max(emotions, key=emotions.get)
    #max_emotion_score = emotions[max_emotion]
    formated_dict_emotions = {
                            'anger': anger,
                            'disgust': disgust,
                            'fear': fear,
                            'joy': joy,
                            'sadness': sadness,
                            'dominant_emotion': max_emotion
                            }
    return formated_dict_emotions