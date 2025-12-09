import pytest
import requests

class TestAPIAccountCreate:
    @pytest.mark.parametrize("request_data", [
        {
            "name": "John",
            "surname": "Doe",
            "pesel": "12345678901",
            "promocode": "PROM_O10"
        },
        {
            "name": "Alice",
            "surname": "Smith",
            "pesel": "10987654321"
        }
    ])
    def test_successful_create_account(self, request_data, API_base_url):
        response = requests.post(f"{API_base_url}/accounts", json=request_data)
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Account created"
    @pytest.mark.parametrize("request_data", [
        {
            "name": "John",
            "surname": "Doe",
            "pesel": "12345678901",
            "promocode": "PROM_O10"
        }
    ])
    def test_duplicate_create_account(self, request_data, API_base_url):
        response = requests.post(f"{API_base_url}/accounts", json=request_data)
        duplicate_response = requests.post(f"{API_base_url}/accounts", json=request_data)
        assert duplicate_response.status_code == 409
        data = duplicate_response.json()
        assert data["error"] == "Account with this PESEL already exists"
        
    