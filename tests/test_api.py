import requests
from requests.exceptions import ConnectionError


def set_api_port() -> int:

    try:
        resp = requests.get("http://localhost:8000/api/v1/status")
        api_port = 8000
    except ConnectionError:
        resp = requests.get("http://localhost:8001/api/v1/status")
        api_port = 8001
    except Exception as error:
        raise error

    return api_port


def test_api_v1_chat():

    port = set_api_port()
    url = f"http://localhost:{port}/v1/chat"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "message": "Good morning, little hobbit!",
        "personality": "Frodo Baggins"
    }

    # Make the POST request
    response = requests.post(url=url, headers=headers, json=data)

    assert response.status_code == 200

    pass
