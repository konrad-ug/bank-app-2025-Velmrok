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
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(-amount)
    def express_withdraw(self, amount, fee):
        total_amount = amount + fee
        if 0 < amount <= self.balance:
            self.balance -= total_amount
            self.history.append(-amount)
            self.history.append(-fee)
    