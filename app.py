import os
import json
import pandas as pd
from flask import Flask, request
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json

app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def prediction():
    if "sentence" not in request.args:
        return "Precondition Failed", 412
    text = request.args["sentence"]
    model = load_model("src/toxic_gauge.h5")
    with open("src/tokenizer.json") as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    padded_text = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=100)
    prediction = model.predict(padded_text)
    response = {
        "toxic": str(prediction[0][0]),
        "severe_toxic": str(prediction[0][1]),
        "obscene": str(prediction[0][2]),
        "threat": str(prediction[0][3]),
        "insult": str(prediction[0][4]),
        "identity_hate": str(prediction[0][5]),
    }
    return json.dumps(response, indent=4), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))