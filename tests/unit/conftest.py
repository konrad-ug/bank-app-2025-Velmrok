from unittest.mock import patch
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

################################### AccountRegistry
@pytest.fixture
def empty_registry():
    return AccountRegistry()
@pytest.fixture
def populated_registry():
    registry = AccountRegistry()
    account1 = PersonalAccount("Alice", "Personal", "12345678901")
    account2 = PersonalAccount("Bob", "Personal", "10987654321")
    registry.add_account(account1)
    registry.add_account(account2)
    return registry
#################################### Bank
@pytest.fixture
def bank():
    b = PersonalAccount("Bank", "Service", "00000000000")
    b.balance = 10000.0
    b.history = []
    return b
################################ Mock API Requests for CompanyAccount
@pytest.fixture(autouse=True)
def mock_api_requests():
    with patch('src.company_account.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'statusVat': 'Czynny'}
        yield mock_get