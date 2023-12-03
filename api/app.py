import numpy as np
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import re
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app, origins=["*"], allow_headers=["*"], methods=["GET", "POST", "PUT", "DELETE", "PATCH"])

logistic_regression = pickle.load(open('models/logistic_regression_model.pkl', 'rb'))

dataset = pd.read_csv('emails.csv')
data = dataset.copy().drop(columns='Email No.')
X = data.drop(columns=['Prediction'])

def preprocess_input_string(input_string, columns):
    # Tokenize the input string and count the occurrence of each word
    # remove all non-alphanumeric characters but keep spaces
    input_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    word_list = input_string.lower().split()
    word_count = {word: word_list.count(word) for word in word_list}

    # Create a DataFrame with zeros for all columns
    input_df = pd.DataFrame(columns=columns)
    input_df.loc[0] = [0] * len(columns)

    # Update the DataFrame with word counts from the input string
    for word in word_count:
        if word in input_df.columns:
            input_df.at[0, word] = word_count[word]

    return input_df

def predict_string(input_string):
    # Load the trained model
    loaded_model = pickle.load(open('models/logistic_regression_model.pkl', 'rb'))

    # Preprocess the input string to match the dataset's format
    processed_input_df = preprocess_input_string(input_string, X.columns)

    # Make a prediction using predict_proba
    probabilities = loaded_model.predict_proba(processed_input_df)

    # Extract the probability of the positive class
    positive_class_probability = probabilities[0][1]
    return positive_class_probability

@app.route('/live', methods=['GET'])
def live():
    return "Live"

@app.route('/predict/logistic',methods=['POST'])
def predict_logistic():
    '''
    For rendering results with JSON
    '''
    data = request.get_json(force=True)
    prediction = predict_string(data['input'])
    return jsonify({'logistic': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)