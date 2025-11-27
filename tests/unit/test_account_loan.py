from src.personal_account import PersonalAccount
import pytest

class TestAccountLoan:

    def create_account(self, history):
        account = PersonalAccount("Loan", "Tester", "85010112345")
        account.history = history
        account.balance = 0.0
        return account

    @pytest.mark.parametrize("history, amount, should_succeed", [
        ([100, 200, 150], 300,True), 
        ([100, 100, 100, 100, 100], 200, True), 
        ([100, 100, 100, -100, 200], 300, True), 
        ([100, 100, 100, -100, 100], 600, False), 
        ([100, 100, 800, -100], 600, False),
        ([], 100, False)
    ])
    def test_loan(self, bank, history, amount,should_succeed):
        account = self.create_account(history)
        result = account.submit_for_loan(bank, amount)
        if should_succeed:
            assert result is True
            assert account.balance == amount
            assert bank.history[-1] == -amount
        else:
            assert result is False
            assert account.balance == 0.0
            assert bank.history == []
    @pytest.mark.parametrize("history,should_succeed", [([100, 200, 150], True), ([100, -50, 200], False)])
    def test_recent_history(self, history, should_succeed):
        account = PersonalAccount("Test", "User", "80010112345")
        account.history = history
        assert account.has_positive_recent_history() is should_succeed
  
    @pytest.mark.parametrize("history,amount,should_succeed", [
        ([100, 200, 200, 300, 400], 1000, True),
        ([100, 100, 100, 100, 100], 600, False)
    ])
    def test_five_payments_exceeding_amount(self, history, amount, should_succeed):
        account = PersonalAccount("Test", "User", "80010112345")
        account.history = history
        assert account.has_five_payments_exceeding_amount(amount) is should_succeed


