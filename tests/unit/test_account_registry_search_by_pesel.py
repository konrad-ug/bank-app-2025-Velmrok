from personal_account import PersonalAccount
from account_registry import AccountRegistry
import pytest
class TestAccountRegistrySearchByPesel:

    def test_search_existing_account(self, populated_registry):
        found_account = populated_registry.find_account_by_pesel("12345678901")
        found_account2 = populated_registry.find_account_by_pesel("10987654321")
        assert found_account2 == populated_registry.accounts[1]
        assert found_account == populated_registry.accounts[0]
    @pytest.mark.parametrize("pesel", [
        "00000000000","123","abcdfghjkfl",None
    ])
    def test_search_nonexistent_account(self, populated_registry, pesel):
        found_account = populated_registry.find_account_by_pesel(pesel)
        assert found_account is None
    def test_search_empty_registry(self, empty_registry):
        found_account = empty_registry.find_account_by_pesel("12345678901")
        assert found_account is None