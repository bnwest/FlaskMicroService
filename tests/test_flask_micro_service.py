import requests


def test_hello_word():
    r = requests.get("http://flask_micro_service:5000/hello")
    assert r.status_code == 200
    response_str = r.json()
    assert type(response_str) == str
    assert response_str.find('Hello World') >= 0


def test_get_versions():
    r = requests.get("http://flask_micro_service:5000/get_versions")
    assert r.status_code == 200
    response_json = r.json()
    assert type(response_json) == dict
    assert 'python' in response_json
    assert 'flask' in response_json
    assert 'flask_restplus' in response_json
    assert 'marshmallow' in response_json


def test_echo():
    r = requests.get("http://flask_micro_service:5000/echo", json={"answer": 42})
    assert r.status_code == 200
    response_json = r.json()
    assert type(response_json) == dict
    assert 'answer' in response_json
    assert response_json['answer'] == 42


def test_echo_plus():
    r = requests.get("http://flask_micro_service:5000/echo_plus", json={"answer": 42})
    assert r.status_code == 200
    response_json = r.json()
    assert type(response_json) == dict
    assert 'answer' in response_json
    assert response_json['answer'] == 42
    assert 'utc' in response_json
    assert 'utc_alt' in response_json
