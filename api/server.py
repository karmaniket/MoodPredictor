import os
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__, static_folder='../static', template_folder='../templates')

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_mood', methods=['POST'])
def predict_mood():
    data = request.json
    text = data['text']
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    response = {'mood': prediction[0]}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
