from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

class TestAccountRegistryClearAllAccounts:
    def test_clear_all_accounts_removes_all_accounts(self):
        registry = AccountRegistry()
        acc1 = PersonalAccount("Jan", "Kowalski", "12345678901")
        acc2 = PersonalAccount("Anna", "Nowak", "10987654321")
        registry.add_account(acc1)
        registry.add_account(acc2)

        assert len(registry.get_all_accounts()) == 2

        registry.clear_accounts()

        assert len(registry.get_all_accounts()) == 0