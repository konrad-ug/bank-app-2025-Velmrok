import pytest
import requests
################################### AccountRegistry
@pytest.fixture()
def request_data():
    return {
        "name": "John",
        "surname": "Doe",
        "pesel": "12345678901",
        "promocode": "PROM_O10"
    }
@pytest.fixture()
def API_base_url():
    return "http://localhost:5000/api"
@pytest.fixture(autouse=True)
def clear_registry_after_test(API_base_url):
    yield
    requests.post(f"{API_base_url}/accounts/clear") 