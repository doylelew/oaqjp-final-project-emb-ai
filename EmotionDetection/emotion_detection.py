import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    INPUT = { "raw_document": { "text": text_to_analyse } }
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json = INPUT, headers=HEADER)
    return (response.status_code, response.text)

def emotion_predictor(text_to_analyse):
    status_code, response_dict = emotion_detector(text_to_analyse)
    if status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotion_results = json.loads(response_dict)['emotionPredictions'][0]['emotion']
    
    max = 0
    dominant_emotion = None

    for key in emotion_results:
        if emotion_results[key] > max:
            max =emotion_results[key]
            dominant_emotion = key
        
    emotion_results['dominant_emotion'] =dominant_emotion

    return emotion_results

if __name__ == "__main__":
    text = " "
    print(text)
    print(emotion_predictor(text))
