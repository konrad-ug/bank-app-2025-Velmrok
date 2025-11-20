import pytest
from company_account import CompanyAccount

@pytest.fixture
def company_accounts():
    sender = CompanyAccount("Test Company Sender", "1234567890")
    receiver = CompanyAccount("Test Company Receiver", "0987654321")
    receiver.balance = 0.0
    return sender, receiver

class TestCompanyAccountExpressTransfer:

   
    @pytest.mark.parametrize("amount, initial_balance, should_succeed", [
        (50.0, 100.0, True), 
        (50.0, 50.0, True),
         (56.0, 55.0, False),   
        (-10.0, 100.0, False), 
        (0.0, 100.0, False),   
     
    ])
    def test_express_transfer(self,
         company_accounts, amount, initial_balance, should_succeed):
        sender, receiver = company_accounts
        sender.balance = initial_balance
        
        sender.express_transfer(receiver, amount)
        if should_succeed:
            assert sender.balance == initial_balance - amount - 5.0
            assert receiver.balance == amount
        else:
            assert sender.balance == initial_balance
            assert receiver.balance == 0.0
    def test_express_transfer_to_self(self, company_accounts):
        sender, _ = company_accounts
        sender.balance = 100.0
        sender.express_transfer(sender, 50.0)
        assert sender.balance == 100.0