import pytest
import requests
import random
import json

@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breweries
def test_openbrewerydb_api_breweries(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breweries"
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breweries c параметрами поиска
@pytest.mark.parametrize('query_parametr', ['by_city=san_diego', 'by_dist=38.8977,77.0365', 'by_name=cooper',
                                            'by_state=ohio', 'by_postal=44107', 'page=15', 'per_page=25'])
def test_openbrewerydb_api_breweries_parametr(base_api_url, status_code, query_parametr):
    res = requests.get(
        base_api_url + "/breweries?" + query_parametr
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breweries c параметрами поиска и
# сортировкой по типу
@pytest.mark.parametrize('type_parametr',
                         ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar',
                          'contract', 'closed', pytest.param('proprietor', marks=pytest.mark.xfail(reason='some bug'))],
                         )
def test_openbrewerydb_api_breweries_type(base_api_url, status_code, type_parametr):
    res = requests.get(
        base_api_url + "/breweries?by_type=" + type_parametr
    )
    status_code_get = res.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breweries по определённой пивоварне
def test_openbrewerydb_api_breweries_one(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breweries"
    )
    get_id_brewery = res.json()
    id_brewery = get_id_brewery[random.randint(0, 5)]['id']  # Получение id пивоварни (предполагается что в запросе
    # будет минимум 5 пивоварен)
    res_2 = requests.get(
        base_api_url + "/breweries/" + str(id_brewery)
    )
    status_code_get = res_2.status_code
    assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тест на корректность поиска методом autocomplete
def test_openbrewerydb_api_breweries_autocomplete(base_api_url, status_code):
    res = requests.get(
        base_api_url + "/breweries"
    )
    get_name_brewery = res.json()
    name_brewery = get_name_brewery[random.randint(0, 5)]['name']  # Получение названия пивоварни (предполагается что в
    # ответе будет минимум 5 пивоварен)
    res_2 = requests.get(
        base_api_url + "/breweries/autocomplete?query=" + str(name_brewery)
    )
    result_autocomplete = res_2.json()
    name_brewery_search = result_autocomplete[0]['name']  # Получение названия пивоварни после поиска
    assert name_brewery_search == name_brewery