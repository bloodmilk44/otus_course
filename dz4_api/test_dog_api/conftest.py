import pytest


# Test API: https://dog.ceo/api/breeds
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo/api",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def base_api_url(request):
    return request.config.getoption("--url")
