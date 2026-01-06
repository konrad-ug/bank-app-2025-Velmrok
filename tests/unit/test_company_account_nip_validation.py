import pytest
from unittest.mock import patch
from src.company_account import CompanyAccount


def test_validate_nip_existance_returns_true_when_active():
    nip = "1234567890"
    account = CompanyAccount("Test Company", nip)
    
    with patch('src.company_account.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'statusVat': 'Czynny'}
        result = account.validate_nip_existance()
        assert result is True


def test_validate_nip_existance_raises_error_when_not_active():
    nip = "1234567890"
    account = CompanyAccount("Not Active", nip)

    with patch('src.company_account.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'statusVat': 'Zwolniony'}

        with pytest.raises(ValueError, match="Company not registered!!"):
            account.validate_nip_existance()


def test_validate_nip_existance_returns_false_on_api_error():
    nip = "1234567890"
    account = CompanyAccount("Error", nip)

    with patch('src.company_account.requests.get') as mock_get:
        mock_get.return_value.status_code = 500 
        result = account.validate_nip_existance()
        assert result is False
def test_validate_nip_existance_returns_false_on_invalid_nip():
    nip = "Invalid"
    account = CompanyAccount("Invalid", nip)

    result = account.validate_nip_existance()
    assert result is False