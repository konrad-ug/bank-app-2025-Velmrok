import requests

class TestAPISaveAndLoadRegistry:
    def test_save_and_load_registry(self,API_base_url):
        account_data = {
            "name": "test",
            "surname": "Testowa",
            "pesel": "11111111111",
            "promocode": ""
        }
        resp = requests.post(f"{API_base_url}/accounts", json=account_data)
        assert resp.status_code == 201

        resp = requests.get(f"{API_base_url}/accounts/count")
        assert resp.json()["count"] == 1

        resp = requests.post(f"{API_base_url}/accounts/save")
        assert resp.status_code == 200

        resp = requests.post(f"{API_base_url}/accounts/clear")
        assert resp.status_code == 200
        
        resp = requests.get(f"{API_base_url}/accounts/count")
        assert resp.json()["count"] == 0

        resp = requests.post(f"{API_base_url}/accounts/load")
        assert resp.status_code == 200

        resp = requests.get(f"{API_base_url}/accounts/count")
        assert resp.json()["count"] == 1

        resp = requests.get(f"{API_base_url}/accounts/11111111111")
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "test"
        assert data["surname"] == "Testowa"