from flask.cli import load_dotenv
from src.base_account import BaseAccount
from datetime import date
import requests
import os
load_dotenv()
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
    def take_loan(self, bank, amount):
        if self.balance >= amount*2 and -1775 in self.history:
            bank.transfer(self, amount)
            return True
        return False
    def validate_nip_existance(self):
        nip_str = str(self.nip)
        if(nip_str == "Invalid"):
            return False
        current_date = date.today().isoformat()
        mf_url = os.environ.get("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
        response = requests.get(f"{mf_url}/api/search/nip/{nip_str}?date={current_date}")
        if response.status_code != 200:
            return False
        data = response.json()
        if data is None or 'statusVat' not in data:
            return False
        if data['statusVat'] != "Czynny":
            raise ValueError("Company not registered!!")
        print("NIP is active")
        return True