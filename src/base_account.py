class BaseAccount:
    def __init__(self, saldo=0.0):
        self.balance = saldo

    def transfer(self, receiver_account, amount):
        if amount <= 0 or self == receiver_account:
            return
        if self.balance >= amount:
            self.balance -= amount
            receiver_account.balance += amount