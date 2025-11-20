from account import Account
import pytest

class TestAccountLoan:
    @pytest.fixture
    def bank(self):
        b = Account("Bank", "Service", "00000000000")
        b.balance = 10000.0
        b.history = []
        return b

    def create_account_with_history(self, history):
        account = Account("Loan", "Tester", "85010112345")
        account.history = history
        account.balance = 0.0
        return account

    @pytest.mark.parametrize("history, amount, should_succeed", [
        ([100, 200, 150], 300,True),
        ([100, 100, 100, 100, 100], 200, True),
        ([100, 100, 100, -100, 200], 300, True),
        ([100, 100, 100, -100, 100], 600, False),
        ([100, 100, 800, -100], 600, False),
        ([100, -50, 200], 200, False),
        ([], 100, False)
    ])
    def test_loan(self, bank, history, amount,should_succeed):
        account = self.create_account_with_history(history)
        result = account.submit_for_loan(bank, amount)
        if should_succeed:
            assert result is True
            assert account.balance == amount
            assert bank.history[-1] == -amount
        else:
            assert result is False
            assert account.balance == 0.0
            assert bank.history == []



