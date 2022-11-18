import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
import requests
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def home1():
    return render_template("index.html")

@app.route('/predict')
def home2():
    return render_template("web.html")

@app.route('/login', methods=['POST'])
def login():
    x_input = str(request.form['price'])
    x_input = x_input.split(',')
    print(x_input)
    for i in range(0, len(x_input)):
        x_input[i] = float(x_input[i])
    print(x_input)

    t = [[[x_input[0]], [x_input[1]], [x_input[2]], [x_input[3]], [x_input[4]], [x_input[5]], [x_input[6]], [x_input[7]], [x_input[8]], [x_input[9]]]]

    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "XaiBJfyOLdZqFSL97wZAhSDoUywnhzRwIepZ9Xdasmbi"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10"],
                                       "values": t }]}

    response_scoring = requests.post(
        'https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/a9cb2f00-3b73-4b0b-8c9f-76c646e8acf4/predictions?version=2022-11-18',
        json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})

    prediction = response_scoring.json()

    p = prediction['predictions'][0]['values'][0][0]

    return render_template("web.html", showcase = 'The next day predicted value is: ' + str(p))

if __name__ == '__main__':
    app.run(debug=True, port=5000)