from account_registry import AccountRegistry
from personal_account import PersonalAccount
import pytest


class TestAccountRegistryAddAccount:
   
    def test_add_single_account(self, empty_registry):
        account = PersonalAccount("Alice", "Personal", "12345678901")
        empty_registry.add_account(account)
        assert account in empty_registry.get_all_accounts()
    def test_add_multiple_accounts(self, empty_registry):
        account1 = PersonalAccount("Bob", "Personal", "10987654321")
        account2 = PersonalAccount("Charlie", "Personal", "11223344556")
        empty_registry.add_account(account1)
        empty_registry.add_account(account2)
        assert account1 in empty_registry.get_all_accounts()
        assert account2 in empty_registry.get_all_accounts()
    def test_add_duplicate_account(self, empty_registry):
        account1 = PersonalAccount("David", "Personal", "22334455667")
        account2 = PersonalAccount("Eve", "Personal", "22334455667")  
        empty_registry.add_account(account1)
        with pytest.raises(ValueError) as excinfo:
            empty_registry.add_account(account2)
        assert "Account with PESEL 22334455667 already exists." in str(excinfo.value)
    def test_add_null_account(self, empty_registry):
        with pytest.raises(ValueError) as excinfo:
            empty_registry.add_account(None)
        assert "Cannot add a null account." in str(excinfo.value)
        