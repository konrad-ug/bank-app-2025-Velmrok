import pytest
import requests
@pytest.fixture()
def API_base_url():
    return "http://127.0.0.1:5000/api"