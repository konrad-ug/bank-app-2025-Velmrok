import pytest
import requests

class TestAPIAccountTransfer:
    @pytest.fixture
    def create_account(self, request_data, API_base_url):
        create_response = requests.post(f"{API_base_url}/accounts", json=request_data)
        transfer_response = requests.post(f"{API_base_url}/accounts/{request_data['pesel']}/transfer", json={
            "amount": 100.0,
            "type": "incoming"
        })
        assert transfer_response.status_code == 200
        assert create_response.status_code == 201
        return request_data
    @pytest.mark.parametrize("withdraw_amount,should_succeed",
         [(25.5, True), (100.0, True), (150.0, False), (0.0, False), (-20.0, False)])
    def test_withdraw(self, create_account, API_base_url, withdraw_amount, should_succeed):
        pesel = create_account['pesel']
        request_data = {"amount": withdraw_amount,"type":"outgoing"}
        withdraw_response = requests.post(f"{API_base_url}/accounts/{pesel}/transfer", json=request_data)
        balance = withdraw_response.json()['balance']
        if should_succeed:
            assert withdraw_response.status_code == 200
            assert balance + withdraw_amount == 100.0
        else:
            assert withdraw_response.status_code == 422
            assert balance == 100.0
    @pytest.mark.parametrize("deposit_amount,should_succeed",
         [(25.5, True), (100.0, True), (0.0, False), (-20.0, False)])
    def test_deposit(self, create_account, API_base_url, deposit_amount, should_succeed):
        pesel = create_account['pesel']
        request_data = {"amount": deposit_amount,"type":"incoming"}
        deposit_response = requests.post(f"{API_base_url}/accounts/{pesel}/transfer", json=request_data)
        balance = deposit_response.json()['balance']
        if should_succeed:
            assert deposit_response.status_code == 200
            assert balance - deposit_amount == 100.0
        else:
            assert deposit_response.status_code == 422
            assert balance== 100.0
    @pytest.mark.parametrize("withdraw_amount,should_succeed",
         [(25.5, True), (100.0, True), (101.0, False), (0.0, False), (-20.0, False)])
    def test_express_withdraw(self, create_account, API_base_url, withdraw_amount, should_succeed):
        pesel = create_account['pesel']
        request_data = {"amount": withdraw_amount,"type":"express"}
        withdraw_response = requests.post(f"{API_base_url}/accounts/{pesel}/transfer", json=request_data)
        balance = withdraw_response.json()['balance']
        if should_succeed:
            assert withdraw_response.status_code == 200
            assert balance + withdraw_amount + 1.0 == 100.0
        else:
            assert withdraw_response.status_code == 422
            assert balance == 100.0
    def test_wrong_transfer_type(self, create_account, API_base_url):
        pesel = create_account['pesel']
        request_data = {"amount": 50.0,"type":"invalid_type"}
        transfer = requests.post(f"{API_base_url}/accounts/{pesel}/transfer", json=request_data)
        balance = transfer.json()['balance']
        assert transfer.status_code == 400
        assert balance == 100.0
   

