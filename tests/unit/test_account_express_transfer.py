from account import Account
class TestAccountExpressTransfer:
    def test_express_transfer(self):
        sender = Account("Jack", "Black", "67890123456")
        receiver = Account("Kara", "White", "54321098765")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == 49.0  # 50 + 1 fee
        assert receiver.balance == 50.0
    def test_express_transfer_insufficient_funds_for_fee(self):
        sender = Account("Liam", "Gray", "78901234567")
        receiver = Account("Mia", "Blue", "65432109876")
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == -1.0  
        assert receiver.balance == 50.0
    def test_express_transfer_negative_amount(self):
        sender = Account("Nina", "Yellow", "89012345678")
        receiver = Account("Owen", "Orange", "76543210987")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, -10.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_express_transfer_to_self(self):
        account = Account("Paul", "Purple", "90123456789")
        account.balance = 100.0
        account.express_transfer(account, 50.0)
        assert account.balance == 100.0
    def test_express_transfer_zero_amount(self):
        sender = Account("Quinn", "Cyan", "01234567890")
        receiver = Account("Rita", "Magenta", "87654321098")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 0.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_express_transfer_insufficient_funds(self):
        sender = Account("Liam", "Gray", "78901234567")
        receiver = Account("Mia", "Blue", "65432109876")
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 51.0)
        assert sender.balance == 50.0
        assert receiver.balance == 0.0