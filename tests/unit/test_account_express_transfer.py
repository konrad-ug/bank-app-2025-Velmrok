import pytest
from personal_account import PersonalAccount



class TestAccountExpressTransfer:
    @pytest.fixture
    def accounts(self):
        sender = PersonalAccount("John", "Doe", "12345678901")
        receiver = PersonalAccount("Jane", "Doe", "10987654321")
        receiver.balance = 0.0
        return sender, receiver
    @pytest.mark.parametrize(
    "amount, initial_balance, should_succeed",
    [
        (50.0, 100.0, True),
        (50.0, 50.0, True),
        (51.0, 50.0, False),
        (-10.0, 100.0, False),
        (0.0, 100.0, False),
    ]
    )
    def test_express_transfer(self, accounts, amount, initial_balance, should_succeed):
        sender, receiver = accounts
        sender.balance = initial_balance
        sender.express_transfer(receiver, amount)

        if should_succeed:
            assert sender.balance == initial_balance - amount - 1.0
            assert receiver.balance == amount
        else:
            assert sender.balance == initial_balance
            assert receiver.balance == 0.0

    def test_express_transfer_to_self(self, accounts):
        sender, _ = accounts
        sender.balance = 100.0
        sender.express_transfer(sender, 50.0)
        assert sender.balance == 100.0