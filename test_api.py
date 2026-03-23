import requests

url = "http://127.0.0.1:5000/predict"

while True:
    user_input = input("\nEnter email text (or type 'exit'): ")

    if user_input.lower() == "exit":
        break

    data = {
        "text": user_input
    }

    response = requests.post(url, json=data)

    print("Response:", response.json())