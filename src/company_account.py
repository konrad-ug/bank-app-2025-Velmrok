from base_account import BaseAccount
class CompanyAccount(BaseAccount):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.nip = nip
        self.validate_nip()
    def validate_nip(self):
        nip_str = str(self.nip)
        if len(nip_str) != 10 or not nip_str.isdigit():
            self.nip = "Invalid"
            return False
        return True
    def express_transfer(self, receiver_account, amount):
        super().express_transfer(receiver_account, amount, 5)
    
