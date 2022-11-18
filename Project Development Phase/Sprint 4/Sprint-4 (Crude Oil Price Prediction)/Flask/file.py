import requests
import numpy as np
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "XaiBJfyOLdZqFSL97wZAhSDoUywnhzRwIepZ9Xdasmbi"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "n10"], "values": [[[25.56], [26], [26.53], [25.85], [25.87], [26.03], [25.65], [25.08], [24.97], [25.18]]]}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/a9cb2f00-3b73-4b0b-8c9f-76c646e8acf4/predictions?version=2022-11-18', json=payload_scoring,  headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
prediction = response_scoring.json()
print("Next Day Predicted Price is: ", prediction['predictions'][0]['values'][0][0])
