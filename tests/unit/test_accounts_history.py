from account import Account
from company_account import CompanyAccount
class BaseAccountTests:
    def test_account_history_after_sent_transfer(self):
        sender, receiver = self.make_accounts()
        sender.transfer(receiver, 500.0)
        assert -500 in sender.history
    def test_account_history_after_received_transfer(self):
        sender, receiver = self.make_accounts()
        sender.transfer(receiver, 500.0)
        assert 500 in receiver.history

class TestAccountHistory(BaseAccountTests):
    def make_accounts(self):
        sender = Account("Alice", "Smith", "12345678901")
        receiver = Account("Bob", "Johnson", "10987654321")
        sender.balance = 500.0
        sender.history = []
        return sender, receiver
    
    def test_account_history_sent_express_transfer(self):
        sender, receiver = self.make_accounts()
        sender.express_transfer(receiver, 500.0)
        assert -500 in sender.history
        assert -1 in sender.history

class TestCompanyAccountHistory(BaseAccountTests):
    def make_accounts(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company2", "1234567890")
        sender.balance = 500.0
        sender.history = []
        return sender, receiver
    
    def test_account_history_sent_express_transfer(self):
        sender, receiver = self.make_accounts()
        sender.express_transfer(receiver, 500.0)
        assert -500 in sender.history
        assert -5 in sender.history


