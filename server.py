"""
server.py : Main module for the Flask application.

This module sets up a Flask server with endpoints, including one for 
emotion detection using the emotion_detector function from the 
EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """ 
    server.py : Main module for Flask app
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {response['anger']},
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},
    and 'sadness': {response['sadness']}. The dominant emotion is
        {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    """
    Function to render the web app template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
