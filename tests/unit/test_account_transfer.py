import pytest
from account import Account 

@pytest.fixture
def accounts():
    sender = Account("Alice", "Smith", "12345678901")
    receiver = Account("Bob", "Johnson", "10987654321")
    sender.balance = 100.0
    receiver.balance = 0.0
    return sender, receiver

class TestAccountTransfer:
    def test_successful_transfer(self, accounts):
        sender, receiver = accounts
        sender.transfer(receiver, 50.0)
        assert sender.balance == 50.0
        assert receiver.balance == 50.0

    @pytest.mark.parametrize("transfer_amount, initial_balance", [
        (50.0, 30.0),   
        (-20.0, 100.0), 
        (0.0, 100.0),   
    ])
    def test_failed_transfer_scenarios(self, accounts, transfer_amount, initial_balance):
        sender, receiver = accounts
        sender.balance = initial_balance
        sender.transfer(receiver, transfer_amount)
        assert sender.balance == initial_balance
        assert receiver.balance == 0.0

    def test_transfer_to_self(self, accounts):
        sender, _ = accounts
        sender.transfer(sender, 50.0)
        assert sender.balance == 100.0

