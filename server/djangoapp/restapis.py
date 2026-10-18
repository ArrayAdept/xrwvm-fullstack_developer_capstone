import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://127.0.0.1:3030")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "?" + "&".join([f"{key}={value}" for key, value in kwargs.items()])

    request_url = backend_url.rstrip('/') + endpoint + params

    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return []

def analyze_review_sentiments(text):
    return {"sentiment": "neutral"}

def post_review(data_dict):
    request_url = backend_url.rstrip('/') + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None
