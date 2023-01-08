import requests
import json

#from sqlalchemy.orm import Session

#from app import models
#from app import database


def test_get_random_gamemode():
    response = requests.get('http://127.0.0.1:8000/gamemode')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["gamemode_name"]) == str
    assert 0 <= response_dictionary["gamemode_id"] <= 100


def test_get_random_class():
    response = requests.get('http://127.0.0.1:8000/class')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["class_name"]) == str
    assert 0 <= response_dictionary["class_id"] <= 100


def test_get_random_location():
    response = requests.get('http://127.0.0.1:8000/location')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["location_name"]) == str
    assert type(response_dictionary["zip"]) == int
    assert type(response_dictionary["city"]) == str
    assert 0 <= response_dictionary["location_id"] <= 100


def test_get_gamemodes():
    response = requests.get('http://127.0.0.1:8000/gamemodes/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for gamemode in response_dictionary:
        assert type(gamemode["gamemode_name"]) == str
    for gamemodeid in response_dictionary:
        assert type(gamemodeid["gamemode_id"]) == int
        assert 0 <= gamemodeid["gamemode_id"] <= 100


def test_get_classes():
    response = requests.get('http://127.0.0.1:8000/classes/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for wclass in response_dictionary:
        assert type(wclass["class_id"]) == int
        assert 0 <= wclass["class_id"] <= 100
    for class_name in response_dictionary:
        assert type(class_name["class_name"]) == str


def test_get_locations():
    response = requests.get('http://127.0.0.1:8000/locations/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    for locnam in response_dictionary:
        assert type(locnam["location_name"]) == str
    for locid in response_dictionary:
        assert type(locid["location_id"]) == int
        assert 0 <= locid["location_id"] <= 100
    for loczip in response_dictionary:
        assert type(loczip["zip"]) == int
    for city in response_dictionary:
        assert type(city["city"]) == str


def test_post_gamemode():
    test_payload = {"gamemode_name": "Something", "gamemode_key": "smth"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://127.0.0.1:8000/gamemodes/', data=json.dumps(test_payload), headers=headers)
    assert response.status_code == 200
    respons_data = json.loads(response.text)
    assert respons_data["gamemode_name"] == "Something"


def test_post_class():
    test_payload = {"class_name": "Something"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://127.0.0.1:8000/classes/', data=json.dumps(test_payload), headers=headers)
    assert response.status_code == 200
    response_data = json.loads(response.text)
    assert response_data["class_name"] == "Something"


def test_post_location():
    test_payload = {"location_name": "Something", "zip": 1111, "city": "Somewhere"}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://127.0.0.1:8000/locations/', data=json.dumps(test_payload), headers=headers)
    assert response.status_code == 200
    response_data = json.loads(response.text)
    assert response_data["location_name"] == "Something"
    assert response_data["zip"] == 1111
    assert response_data["city"] == "Somewhere"


def test_put_class():
    data = {"class_name": "Nothing"}
    headers = {"Content-Type": "application/json"}
    response = requests.put('http://127.0.0.1:8000/classes/8?class_name=Nothing', data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    response_data = json.loads(response.text)
    assert response_data["class_name"] == "Nothing"


def test_put_gamemodes():
    data = {"gamemode_name": "Nothing"}
    headers = {"Content-Type": "application/json"}
    response = requests.put('http://127.0.0.1:8000/gamemodes/10?gamemode_name=Nothing', data=json.dumps(data),
                            headers=headers)
    assert response.status_code == 200
    response_data = json.loads(response.text)
    assert response_data["gamemode_name"] == "Nothing"


def test_delete_gamemode():
    response = requests.delete("http://127.0.0.1:8000/gamemodes/10/")
    assert response.status_code == 200


def test_delete_class():
    response = requests.delete("http://127.0.0.1:8000/classes/8/")
    assert response.status_code == 200


def test_delete_location():
    response = requests.delete("http://127.0.0.1:8000/locations/8/")
    assert response.status_code == 200








