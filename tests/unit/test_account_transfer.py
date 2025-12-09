import pytest
from src.personal_account import PersonalAccount 

@pytest.fixture
def accounts():
    sender = PersonalAccount("Alice", "Smith", "12345678901")
    receiver = PersonalAccount("Bob", "Johnson", "10987654321")
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
    @pytest.mark.parametrize("withdraw_amount,should_succeed",
            [(50.0, True),{100,True}, (0.0, False), (-10.0, False), (150.0, False)])
    def test_withdraw(self, accounts, withdraw_amount, should_succeed):
        account, _ = accounts
        account.withdraw(withdraw_amount)
        if should_succeed:
            assert account.balance == 100.0 - withdraw_amount
        else:
            assert account.balance == 100.0
    @pytest.mark.parametrize("deposit_amount,should_succeed",
             [(50.0, True), (-1, False), (0.01, True), (0.0, False)])
    def test_deposit(self, accounts, deposit_amount, should_succeed):
        account, _ = accounts
        account.deposit(deposit_amount)
        if should_succeed:
            assert account.balance == 100.0 + deposit_amount
        else:
            assert account.balance == 100.0