import pytest
import requests

class TestAPIAccountUpdate:
    @pytest.mark.parametrize("update_data", [
        {
            "name": "Jane",
            "surname": "Doe-Smith",
        },
        {
            "name": "Bob",
        },
        {
            "surname": "Johnson",
        },
        {}
        ])
    def test_successful_account_update(self, request_data, update_data, API_base_url):

        create_response = requests.post(f"{API_base_url}/accounts", json=request_data)
        assert create_response.status_code == 201
        response = requests.patch(f"{API_base_url}/accounts/{request_data['pesel']}", json=update_data)
        assert response.status_code == 200

        get_response = requests.get(f"{API_base_url}/accounts/{request_data['pesel']}")
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["name"] == update_data["name"] if "name" in update_data else request_data["name"]
        assert data["surname"] == update_data["surname"] if "surname" in update_data else request_data["surname"]