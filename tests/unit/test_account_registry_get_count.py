from src.personal_account import PersonalAccount
from src.account_registry import AccountRegistry

class TestAccountRegistryGetCount:


    def test_get_count(self, populated_registry):
        count = populated_registry.get_count()
        assert count == 2
    def test_get_count_empty_registry(self, empty_registry):
        count = empty_registry.get_count()
        assert count == 0