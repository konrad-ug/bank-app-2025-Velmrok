from base_account import BaseAccount
class PersonalAccount(BaseAccount):
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = self.check_pesel_validity(pesel)
        self.promo_code = promo_code
        self.execute_promo_code(promo_code)
    def calculate_birth_year(self):
        if self.pesel == "Invalid":
            return None
        birth_year = int(str(self.pesel)[0:2])
        month = int(str(self.pesel)[2:4])
        if(month<=12):
            birth_year += 1900
        else:
            birth_year += 2000
        return birth_year
    def check_pesel_validity(self,pesel):
        if len(str(pesel))== 11 and str(pesel).isdigit():
            return pesel
        else:
            return "Invalid"
    def execute_promo_code(self,promo_code):
        birth_year = self.calculate_birth_year()
        if(promo_code is not None
            and len(promo_code) == 8
            and promo_code.startswith("PROM_" )
            and birth_year is not None
            and birth_year > 1960):
            self.balance = 50.0
        else:
            self.promo_code = None
            self.balance = 0.0
    def express_transfer(self, receiver_account, amount):
        super().express_transfer(receiver_account, amount, 1)

    def has_positive_recent_history(self):
        return len(self.history) >= 3 and all(x > 0 for x in self.history[-3:])

    def has_five_payments_exceeding_amount(self, amount):
        return len(self.history) >= 5 and sum(self.history[-5:]) > amount

    def submit_for_loan(self, bank, amount):
        if self.has_positive_recent_history() or self.has_five_payments_exceeding_amount(amount):
            bank.transfer(self, amount)
            return True
        return False
        
       