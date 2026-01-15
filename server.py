from flask import Flask, request, jsonify, render_template_string
import pickle, re, string
import os

# ---------------------- LOAD MODEL ----------------------
with open("../artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("../artifacts/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# ---------------------- CLEAN TEXT FUNCTION ----------------------
def clean_text(t):
    t = t.lower()
    t = re.sub(r"http\S+", " ", t)
    t = t.translate(str.maketrans("", "", string.punctuation))
    t = re.sub(r"\d+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

# ---------------------- FLASK APP ----------------------
app = Flask(__name__)

# ---------------------- FRONTEND HTML ----------------------
with open("../frontend/index.html", "r") as f:
    html_page = f.read()

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.json['message']
    pred = model.predict([clean_text(msg)])
    label = encoder.inverse_transform(pred)[0]
    return jsonify({'prediction': label})

if __name__ == "__main__":
    app.run(debug=True)