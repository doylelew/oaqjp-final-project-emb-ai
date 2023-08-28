import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    INPUT = { "raw_document": { "text": text_to_analyse } }
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json = INPUT, headers=HEADER)
    return response.text

def emotion_predictor(text_to_analyse):
    emotion_results = json.loads(emotion_detector(text_to_analyse))['emotionPredictions'][0]['emotion']
    
    max = 0
    dominant_emotion = None

    for key in emotion_results:
        if emotion_results[key] > max:
            max =emotion_results[key]
            dominant_emotion = key
        
    emotion_results['dominant_emotion'] =dominant_emotion

    return emotion_results

if __name__ == "__main__":
    print(emotion_predictor("I love this new technology"))
