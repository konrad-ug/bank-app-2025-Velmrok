from base_account import BaseAccount
class Account(BaseAccount):
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        if len(str(pesel))== 11 and str(pesel).isdigit():
            self.pesel = pesel
        else:
            self.pesel = "Invalid"
        self.promo_code = promo_code
        if(promo_code is not None
            and len(promo_code) == 8
            and promo_code.startswith("PROM_" )
            and self.pesel != "Invalid"
            and self.calculate_birth_year() > 1960):
            self.balance = 50.0
        else:
            self.promo_code = None
            self.balance = 0.0
    def calculate_birth_year(self):
        birth_year = int(str(self.pesel)[0:2])
        month = int(str(self.pesel)[2:4])
        if(month<=12):
            birth_year += 1900
        else:
            birth_year += 2000
        return birth_year
    def express_transfer(self, receiver_account, amount):
        super().express_transfer(receiver_account, amount, 1)
    def submit_for_loan(self,bank, amount):
        history = self.history
        # Loan is accepted
        if ((len(history) >= 3 and all(x>0 for x in history[-3:]) )
        or (len(history) >=5 and sum(history[-5:]) > amount )):
            bank.transfer(self,amount)
            return True
        else:
            return False
       
       