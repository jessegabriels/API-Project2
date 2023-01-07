import requests
import json


def test_get_random_gamemode():
    response = requests.get('http://127.0.0.1:8000/gamemode')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["gamemode_id"]) == int
    assert 0 <= response_dictionary["gamemode_id"] <= 100

