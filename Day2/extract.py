import requests


def extract_data():

    url = "https://api.github.com"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()