from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def runEmotionDetector():
    q = request.args.get('q')
    if not q: 
        return {"message":"Invalid query."}, 422
    
    result = emotion_detector(q) 

    msg = f"<p>For the given statement, the system response is \
     'anger': {result['anger']} \
     'disgust': {result['disgust']} \
     'fear': {result['fear']} \
     'joy': {result['joy']} and \
     'sadness': {result['sadness']}. \
     The dominant emotion is {result['dominant_emotion']}</p>"

    return {"message":msg}, 200
