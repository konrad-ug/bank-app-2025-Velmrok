import pytest
import requests

class TestAPIPerformance:
    def test_create_delete_loop(self, API_base_url):
        pesel = "04300902156"
        create_payload = {
            "name": "Perf",
            "surname": "Test",
            "pesel": pesel
        }

        for i in range(100):
            response_create = requests.post(f"{API_base_url}/accounts", json=create_payload, timeout=0.5)
            assert response_create.status_code == 201
            assert response_create.elapsed.total_seconds() < 0.5
            response_delete = requests.delete(f"{API_base_url}/accounts/{pesel}", timeout=0.5)
            assert response_delete.status_code == 200
            assert response_delete.elapsed.total_seconds() < 0.5

    def test_transfer_loop(self, API_base_url):
        pesel = "04300902156"
        create_payload = {
            "name": "Perf",
            "surname": "Test",
            "pesel": pesel
        }
        requests.delete(f"{API_base_url}/accounts/{pesel}")
        
        resp = requests.post(f"{API_base_url}/accounts", json=create_payload)
        assert resp.status_code == 201

        transfer_payload = {
            "amount": 10.0,
            "type": "incoming"
        }

        try:
            for i in range(100):
                response = requests.post(
                    f"{API_base_url}/accounts/{pesel}/transfer", 
                    json=transfer_payload, 
                    timeout=0.5
                )
                assert response.status_code == 200
                assert response.elapsed.total_seconds() < 0.5
            response_get = requests.get(f"{API_base_url}/accounts/{pesel}")
            assert response_get.status_code == 200
            data = response_get.json()
            assert data["balance"] == 1000.0

        finally:
            requests.delete(f"{API_base_url}/accounts/{pesel}")
    