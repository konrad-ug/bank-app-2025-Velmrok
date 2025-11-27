from personal_account import PersonalAccount
from account_registry import AccountRegistry
import pytest
class TestAccountRegistryRemoveAccount:

    def test_remove_account(self):
        account = PersonalAccount("Alice", "Personal", "12345678901")
        registry = AccountRegistry()
        registry.add_account(account)
        registry.remove_account(account)
        assert registry.get_count() == 0
        assert registry.find_account_by_pesel("12345678901") is None
    def test_remove_account_empty_registry(self, empty_registry):
        account = PersonalAccount("Alice", "Personal", "12345678901")
        empty_registry.remove_account(account)
        count = empty_registry.get_count()
        assert count == 0