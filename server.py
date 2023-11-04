from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] == None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger': {formated_response['anger']} 'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, 'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. The dominant emotion is {formated_response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)