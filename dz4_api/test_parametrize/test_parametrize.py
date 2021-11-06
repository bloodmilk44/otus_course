import requests


def test_request(base_url, status_code):
    res = requests.get(
        base_url
    )
    assert str(res.status_code) == str(status_code)