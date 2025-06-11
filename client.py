import requests

url = "http://127.0.0.1:8000/predict"
question = {"question": "Quels modes de paiement sont acceptés ?"}
response = requests.post(url, json=question)
print(response.json())
