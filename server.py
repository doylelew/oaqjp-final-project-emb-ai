from flask import Flask, render_template, request
from EmotionDetection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def check_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    json_result = emotion_predictor(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {json_result['anger']}, 'disgust': {json_result['disgust']}, 'fear': {json_result['fear']}, 'joy': {json_result['joy']} and 'sadness': {json_result['sadness']}. The dominant emotion is {json_result['dominant_emotion']}"
    