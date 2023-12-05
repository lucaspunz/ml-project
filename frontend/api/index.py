from flask import Flask, request, jsonify
# from flask_cors import CORS
import pickle
import pandas as pd
import re
# from sklearn.model_selection import train_test_split

app = Flask(__name__)
# CORS(app, origins=["*"], allow_headers=["*"], methods=["GET", "POST", "PUT", "DELETE", "PATCH"])

logistic_regression = pickle.load(open('models/logistic_regression_model.pkl', 'rb'))
naive_bayes = pickle.load(open('models/naive_bayes_model.pkl', 'rb'))
random_forest = pickle.load(open('models/random_forest_model.pkl', 'rb'))

dataset = pd.read_csv('data/emails.csv')
data = dataset.copy().drop(columns='Email No.')
X = data.drop(columns=["Prediction"])
y = data["Prediction"]

clean_dataset = pd.read_csv("data/cleaned_dataset.csv")
X2 = clean_dataset.drop(columns=["Prediction"])
y2 = clean_dataset["Prediction"]
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

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

def predict_string(model, cols, input_string):
    # Preprocess the input string to match the dataset's format
    processed_input_df = preprocess_input_string(input_string, cols)

    # Make a prediction using predict_proba
    probabilities = model.predict_proba(processed_input_df)

    # Extract the probability of the positive class
    positive_class_probability = probabilities[0][1]
    return positive_class_probability

@app.route('/api/live', methods=['GET'])
def live():
    return "Live"

@app.route('/api/predict/all',methods=['POST'])
def predict_all():
    '''
    For rendering results with JSON
    '''
    data = request.get_json(force=True)
    prediction_logistic = predict_string(logistic_regression, X.columns, data['input'])
    prediction_naive_bayes = predict_string(naive_bayes, X2.columns, data['input'])
    prediction_random_forest = predict_string(random_forest, X2.columns, data['input'])

    return jsonify({'logistic': prediction_logistic, 'naive_bayes': prediction_naive_bayes, 'random_forest': prediction_random_forest})

if __name__ == "__main__":
    app.run()