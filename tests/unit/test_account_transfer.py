from account import Account

class TestAccountTransfer:
    def test_successful_transfer(self):
        sender = Account("Alice", "Smith", "12345678901")
        receiver = Account("Bob", "Johnson", "10987654321")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.transfer(receiver, 50.0)
        assert sender.balance == 50.0
        assert receiver.balance == 50.0
    def test_insufficient_funds_transfer(self):
        sender = Account("Charlie", "Brown", "23456789012")
        receiver = Account("Diana", "Prince", "21098765432")
        sender.balance = 30.0
        receiver.balance = 0.0
        sender.transfer(receiver, 50.0)
        assert sender.balance == 30.0
        assert receiver.balance == 0.0
    def test_negative_amount_transfer(self):
        sender = Account("Eve", "Adams", "34567890123")
        receiver = Account("Frank", "Miller", "32109876543")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.transfer(receiver, -20.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    def test_transfer_to_self(self):
        account = Account("Grace", "Hopper", "45678901234")
        account.balance = 100.0
        account.transfer(account, 50.0)
        assert account.balance == 100.0
    def test_transfer_zero_amount(self):
        sender = Account("Hank", "Pym", "56789012345")
        receiver = Account("Ivy", "Green", "43210987654")
        sender.balance = 100.0
        receiver.balance = 0.0
        sender.transfer(receiver, 0.0)
        assert sender.balance == 100.0
        assert receiver.balance == 0.0
    
