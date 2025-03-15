"""
This module is the entry point for the Emotion Detector application.

Returns:
    Flask: The Flask application instance
"""

from flask import Flask, request, render_template
from emotion_detection.emotion_detection import emotion_detector as ed

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_analyzer():
    """
    This function is the entry point for the Emotion Detector application.
    It receives a text string from the user, analyzes the text string and
    returns the emotion detected in the text string.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    emotions = ed(text_to_analyze)

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']

    if dominant_emotion:
        return f"For the given statement, the system response is \
            'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \
            'joy': {joy}, 'sadness': {sadness}. The dominant emotion \
            is <strong>{dominant_emotion}</strong>."
    else:
        return "Invalid text! Please try again"


@app.route("/")
def render_index_page():
    """
    This function renders the index.html page.

    Returns:
        HTML: The index.html page
    """

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
