# app.py
from flask import Flask, request, jsonify
import ml

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Perform prediction with your model
        prediction = ml.predict('data to predict')

        # Return the prediction in JSON format
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})