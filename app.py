from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import re

app = Flask(__name__)

# LOAD DATA
df = pd.read_csv("phishing_email.csv")
df = df.rename(columns={'text_combined': 'text'})
df = df[['text', 'label']]
df = df.dropna()

# TRAIN MODEL
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression()
model.fit(X, y)

# ML PREDICTION
def predict_email(text):
    text_vector = vectorizer.transform([text])
    prob = model.predict_proba(text_vector)[0][1]  # phishing probability
    return prob

# LINK CHECK
def check_links(text):
    urls = re.findall(r'(https?://\S+)', text)
    suspicious = []

    for url in urls:
        if "@" in url or "-" in url or len(url) > 50:
            suspicious.append(url)

    return suspicious

# API ROUTE (IMPORTANT)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    email_text = data.get('text', '')

    prob = predict_email(email_text)
    links = check_links(email_text)

    if prob > 0.85 or len(links) > 0:
        final = "Phishing"
        risk = "High"

    elif prob > 0.60:
        final = "Suspicious"
        risk = "Medium"
    else:
        final = "Safe"
        risk = "Low"

    return jsonify({
        "prediction": final,
        "risk_level": risk,
        "probability": float(prob),
        "suspicious_links": links
})
# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)