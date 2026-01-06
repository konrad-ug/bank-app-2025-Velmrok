import src.smtp.smptp as smtp
from datetime import date
class BaseAccount:
    def __init__(self, saldo=0.0):
        self.balance = saldo
        self.history = []
    def transfer(self, receiver, amount):
        if amount <= 0 or self == receiver:
            return
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.history.append(-amount)
            receiver.history.append(amount)
    def express_transfer(self, receiver, amount, fee):
        total_amount = amount + fee
        if amount <= 0 or self == receiver:
            return
        if self.balance >= amount:
            self.balance -= total_amount
            receiver.balance += amount
            self.history.append(-amount)
            self.history.append(-fee)
            receiver.history.append(amount)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)
        else:
            raise ValueError("Deposit amount must be positive")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(-amount)
        else:
            raise ValueError("Invalid withdraw amount")
    def express_withdraw(self, amount, fee):
        total_amount = amount + fee
        if 0 < amount <= self.balance:
            self.balance -= total_amount
            self.history.append(-amount)
            self.history.append(-fee)
        else:
            raise ValueError("Invalid express withdraw amount")
    def send_history_via_email(self, email_address):
        current_date = date.today().isoformat()
        subject = f"Account Transfer History {current_date}"
        account_type = self.__class__.__name__.replace("Account", " account")
        text = f"{account_type} history: {self.history}"
        return smtp.SMTPClient.send(subject, text, email_address)