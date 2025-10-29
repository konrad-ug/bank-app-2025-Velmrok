from account import Account
class TestAccountExpressTransfer:
    def create_accounts(self):
        sender = Account("John", "Doe", "12345678901")
        receiver = Account("Jane", "Doe", "10987654321")
        return sender, receiver
    def test_express_transfer(self):
        sender, receiver = self.create_accounts()
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == 49.0  # 50 + 1 fee
        assert receiver.balance == 50.0
    def test_express_transfer_insufficient_funds_for_fee(self):
        sender, receiver = self.create_accounts()
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == -1.0  
        assert receiver.balance == 50.0
    def test_express_transfer_negative_amount(self):
        sender, receiver = self.create_accounts()
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
        sender, receiver = self.create_accounts()
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 0.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_express_transfer_insufficient_funds(self):
        sender, receiver = self.create_accounts()
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 51.0)
        assert sender.balance == 50.0
        assert receiver.balance == 0.0