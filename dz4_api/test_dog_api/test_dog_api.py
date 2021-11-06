import pytest
import requests
import random
from jsonschema import validate


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /list/all (получение списка всех
# пород)
def test_dog_api_list_all_breeds(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breeds/list/all"
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [404])  # Тестирование на код ответа метода /list/all (получение списка всех
# пород)
def test_dog_api_list_all_breeds_negative(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breeds/list/all" + str(random.randint(0, 9999))
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])
def test_dog_api_image(base_api_url, status_code):  # Валидация JSON схемы ответа метода /image/random
    res = requests.get(
        base_api_url + "/breeds/image/random"
    )

    schema = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }
    validate(instance=res.json(), schema=schema)
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование запроса разного количества изображений image/random/х
def test_dog_api_ramdom_count_image(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breeds/image/random/" + str(random.randint(1, 10))
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breed/hound/list (получение
# списка всех метисов породы hound
def test_dog_api_list_all_sub_breeds(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breed/hound/list"
    )
    status_code_get = res.status_code
    assert status_code_get == status_code
