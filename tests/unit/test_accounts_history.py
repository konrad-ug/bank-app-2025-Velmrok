import pytest
from personal_account import PersonalAccount
from company_account import CompanyAccount

class BaseAccountHistoryTests:
    @pytest.fixture
    def accounts(self):
        sender = PersonalAccount("Alice", "Smith", "12345678901")
        receiver = PersonalAccount("Bob", "Johnson", "10987654321")
        sender.balance = 500.0
        sender.history = []
        receiver.balance = 0.0
        receiver.history = []
        return sender, receiver

    def test_account_history_after_sent_transfer(self, accounts):
        sender, receiver = accounts
        sender.transfer(receiver, 500.0)
        assert sender.history == [-500]

    def test_account_history_after_received_transfer(self, accounts):
        sender, receiver = accounts
        sender.transfer(receiver, 500.0)
        assert receiver.history == [500]

    def test_account_history_after_self_transfer(self, accounts):
        sender, _ = accounts
        sender.transfer(sender, 100.0)
        assert len(sender.history) == 0
    @pytest.mark.parametrize("transfer_amount, initial_balance", [
        (600.0, 500.0),(-50.0, 500.0),(0.0, 500.0)
    ])
    def test_account_no_history_change_after_failed_transfer(
        self, accounts, transfer_amount, initial_balance ):

        sender, receiver = accounts
        sender.balance = initial_balance
        sender.transfer(receiver, transfer_amount)  
        assert len(sender.history) == 0
        assert len(receiver.history) == 0

class TestAccountHistory(BaseAccountHistoryTests):
    
    def test_account_history_sent_express_transfer(self, accounts):
        sender, receiver = accounts
        sender.express_transfer(receiver, 500.0)
        assert sender.history == [-500, -1]
        assert receiver.history == [500]

    def test_self_express_transfer(self, accounts):
        sender, _ = accounts
        sender.express_transfer(sender, 100.0)
        assert len(sender.history) == 0
    @pytest.mark.parametrize("transfer_amount, initial_balance", [
        (600.0, 500.0),(-50.0, 500.0),(0.0, 500.0)
    ])
    def test_account_no_history_change_after_failed_transfer(
        self, accounts, transfer_amount, initial_balance ):

        sender, receiver = accounts
        sender.balance = initial_balance
        sender.express_transfer(receiver, transfer_amount)  
        assert len(sender.history) == 0
        assert len(receiver.history) == 0

class TestCompanyAccountHistory(BaseAccountHistoryTests):
    @pytest.fixture
    def accounts(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company2", "1234567891")
        sender.balance = 500.0
        sender.history = []
        receiver.balance = 0.0
        receiver.history = []
        return sender, receiver
    
    def test_account_history_sent_express_transfer(self, accounts):
        sender, receiver = accounts
        sender.express_transfer(receiver, 500.0)
        assert sender.history == [-500, -5]
        assert receiver.history == [500]

    def test_self_express_transfer(self, accounts):
        sender, _ = accounts
        sender.express_transfer(sender, 100.0)
        assert len(sender.history) == 0
    @pytest.mark.parametrize("transfer_amount, initial_balance", [
        (600.0, 500.0),(-50.0, 500.0),(0.0, 500.0)
    ])
    def test_account_no_history_change_after_failed_transfer(
        self, accounts, transfer_amount, initial_balance ):

        sender, receiver = accounts
        sender.balance = initial_balance
        sender.express_transfer(receiver, transfer_amount)  
        assert len(sender.history) == 0
        assert len(receiver.history) == 0


