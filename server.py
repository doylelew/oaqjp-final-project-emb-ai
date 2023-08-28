"""
required docstring to get a good grade
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/")
def main_page():
    """
    runs the index.html
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def check_emotion():
    """
    API call to Watson
    """
    text_to_analyze = request.args.get('textToAnalyze')
    json_result = emotion_predictor(text_to_analyze)
    if not json_result['dominant_emotion']:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {json_result['anger']}, "
        f"'disgust': {json_result['disgust']}, 'fear': {json_result['fear']}," 
        f"'joy': {json_result['joy']} and "
        f"'sadness': {json_result['sadness']}." 
        f"The dominant emotion is {json_result['dominant_emotion']}")
    