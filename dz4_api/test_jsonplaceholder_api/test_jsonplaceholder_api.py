import pytest
import requests
import random


@pytest.mark.parametrize('status_code', [200])  # Тест ответа на запрос всех записей
def test_jsonplaceholder_api(base_api_url, status_code):
    res = requests.get(
        base_api_url
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [201])  # Тест POST запроса
def test_jsonplaceholder_api_post(base_api_url, status_code):
    res = requests.post(
        base_api_url,
        data={
            "title": "test",
            "body": "test2",
            "userId": random.randint(100, 1000)
        }
    )
    res_json = res.json()
    status_code_get = res.status_code
    assert status_code_get == status_code
    assert res_json['title'] == 'test'
    assert res_json['body'] == 'test2'


@pytest.mark.parametrize('status_code', [200])  # Тест PUT запроса
def test_jsonplaceholder_api_put(base_api_url, status_code):
    res = requests.put(
        base_api_url + '/1',
        data={
            "title": "test",
            "body": "test2",
            "userId": random.randint(100, 1000)
        }
    )
    res_json = res.json()
    status_code_get = res.status_code
    assert status_code_get == status_code
    assert res_json['title'] == 'test'
    assert res_json['body'] == 'test2'


@pytest.mark.parametrize('status_code', [200])  # Тест PATCH запроса
def test_jsonplaceholder_api_patch(base_api_url, status_code):
    res = requests.patch(
        base_api_url + '/1',
        data={
            "title": "test"
        }
    )
    res_json = res.json()
    status_code_get = res.status_code
    assert status_code_get == status_code
    assert res_json['title'] == 'test'


@pytest.mark.parametrize('status_code', [200])  # Тест DELETE запроса
def test_jsonplaceholder_api_delete(base_api_url, status_code):
    res = requests.delete(
        base_api_url + '/1'
    )
    status_code_get = res.status_code
    assert status_code_get == status_code
    assert res.json() == {}