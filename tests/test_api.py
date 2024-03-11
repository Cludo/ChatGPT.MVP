import requests
from requests.exceptions import ConnectionError


def set_api_port() -> int:
    """
    Sets the port of the API to use for testing.
    This ensures that both local and Dockerized versions of the API can be tested.
    """

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
    """Test the /v1/chat endpoint of the API."""

    #  define the API endpoint
    port = set_api_port()
    url = f"http://localhost:{port}/v1/chat"

    # define request headers
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    # define the input data
    data = {
        "message": "Good morning, little hobbit!",
        "personality": "Frodo Baggins"
    }

    # make the POST request
    response = requests.post(url=url, headers=headers, json=data)

    # assert the response was successful
    assert response.status_code == 200

    pass
