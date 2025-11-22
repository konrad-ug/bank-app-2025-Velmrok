from company_account import CompanyAccount
import pytest


class TestCompanyAccountLoan:
 
    def create_account(self, history,balance):
        account = CompanyAccount("Loan", "85010112345")
        account.history = history
        account.balance = balance
        return account
    @pytest.mark.parametrize("history, balance, amount, should_succeed", [
        ([-1775], 700.0, 300,True),
        ([-1775], 600.0, 300,True),  
        ([1775], 2000.0, 600, False), 
        ([177], 400.0, 200, False),
        ([-1775], 100, 100, False),
        ([], 1000, 100, False)
        
    ])
    def test_loan(self, bank, history, balance, amount,should_succeed):
        account = self.create_account(history,balance)
        result = account.take_loan(bank, amount)
        if should_succeed:
            assert result is True
            assert account.balance == balance + amount
            assert bank.history[-1] == -amount
        else:
            assert result is False
            assert account.balance == balance
            assert bank.history == []