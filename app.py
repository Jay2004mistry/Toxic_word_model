from flask import Flask, request, jsonify, render_template
import joblib
import re

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return " ".join(text.split())

# Homepage
@app.route('/')
def home():
    return render_template("index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    
    prob = model.predict_proba(vec)[0][1]
    score = round(prob * 10)

    if score >= 8:
        result = "Highly Toxic"
    elif score >= 5:
        result = "Toxic"
    else:
        result = "Non-Toxic"

    return render_template("index.html", result=result, score=score)

if __name__ == '__main__':
    app.run(debug=True)