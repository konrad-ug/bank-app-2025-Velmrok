from company_account import CompanyAccount

class TestCompanyAccountExpressTransfer:
    def test_express_transfer(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company", "1234567890")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == 45.0 # 50 + 5 fee
        assert receiver.balance == 50.0
    def test_express_transfer_insufficient_funds_for_fee(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company", "1234567890")
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 50.0)
        assert sender.balance == -5.0  
        assert receiver.balance == 50.0
    def test_express_transfer_negative_amount(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company", "1234567890")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, -10.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_express_transfer_to_self(self):
        account = CompanyAccount("Test Company", "1234567890")
        account.balance = 100.0
        account.express_transfer(account, 50.0)
        assert account.balance == 100.0
    def test_express_transfer_zero_amount(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company", "1234567890")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 0.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_express_transfer_insufficient_funds(self):
        sender = CompanyAccount("Test Company", "1234567890")
        receiver = CompanyAccount("Test Company", "1234567890")
        sender.balance = 50.0
        receiver.balance = 0.0
        sender.express_transfer(receiver, 51.0)
        assert sender.balance == 50.0
        assert receiver.balance == 0.0