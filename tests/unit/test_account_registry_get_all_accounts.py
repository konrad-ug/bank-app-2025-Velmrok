import pytest
from personal_account import PersonalAccount
from account_registry import AccountRegistry

class TestAccountRegistryGetAllAccounts:

    def test_get_all_accounts(self, populated_registry):
        accounts = populated_registry.get_all_accounts()
        assert len(accounts) == populated_registry.get_count()
        pesels = [account.pesel for account in accounts]
        assert "12345678901" in pesels
        assert "10987654321" in pesels
    def test_get_all_accounts_empty_registry(self, empty_registry):
        accounts = empty_registry.get_all_accounts()
        assert accounts == []