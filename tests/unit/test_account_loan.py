from account import Account
import pytest
class TestAccountLoan:
    def create_account_with_history(self, history):
        account = Account("Loan", "Tester", "85010112345")
        account.history = history
        account.balance = 0.0
        return account
    @pytest.fixture
    def bank(self): 
        b = Account("Bank", "Service", "00000000000")
        b.balance = 10000.0
        return b
    def assert_denied_loan(self, account, bank, amount):
        result = account.submit_for_loan(bank, amount)
        assert result == False
        assert account.balance == 0.0
        assert bank.history == []
    def assert_approved_loan(self, account, bank, amount):
        result = account.submit_for_loan(bank, amount)
        assert result == True
        assert bank.history[-1] == -amount
        assert account.balance == amount
    ## TESTS   
    def test_loan_approved_with_three_positive_payments(self, bank):
        account = self.create_account_with_history([100, 200, 150])
        self.assert_approved_loan(account, bank, 300)
    def test_loan_approved_with_five_payments_exceeding_amount(self, bank):
        account = self.create_account_with_history([100,100,100,100,100])
        self.assert_approved_loan(account, bank, 200)
    def test_loan_approved_with_five_payments_exceeding_and_negative_payment(self, bank):
        account = self.create_account_with_history([100, 100, 100, -100, 200])
        self.assert_approved_loan(account, bank, 300)
    def test_loan_approved_with_five_positive_payments_not_exceeding_amount(self, bank):
        account = self.create_account_with_history([100, 100, 100, 100, 100])
        self.assert_approved_loan(account, bank, 600)

    def test_loan_denied_with_negative_payment(self, bank):
        account = self.create_account_with_history([100, -50, 200])
        self.assert_denied_loan(account, bank, 200)
    def test_loan_denied_with_five_payments_not_exceeding_amount(self, bank):
        account = self.create_account_with_history([50, 50, -50, 50, 50])
        self.assert_denied_loan(account, bank, 300)
    def test_loan_denied_with_five_payments_not_exceeding_amount_and_negative_payment(self, bank):
        account = self.create_account_with_history([100, 100,-100,-100,50])
        self.assert_denied_loan(account, bank, 300)
    def test_loan_denied_with_no_history(self, bank):
        account = self.create_account_with_history([])
        self.assert_denied_loan(account, bank, 100)
   
   
       