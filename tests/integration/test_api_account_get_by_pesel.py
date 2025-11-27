import pytest
import requests

class TestAPIAccountGetByPesel:
    def test_successful_get_account(self, request_data, API_base_url):
        create_response = requests.post(f"{API_base_url}/accounts", json=request_data)
        assert create_response.status_code == 201
        response = requests.get(f"{API_base_url}/accounts/{request_data['pesel']}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == request_data["name"]
        assert data["surname"] == request_data["surname"]
        assert data["pesel"] == request_data["pesel"]
    def test_get_account_not_found(self, API_base_url):
        response = requests.get(f"{API_base_url}/accounts/00000000000")
        assert response.status_code == 404
        data = response.json()
        assert data["error"] == "Account not found"