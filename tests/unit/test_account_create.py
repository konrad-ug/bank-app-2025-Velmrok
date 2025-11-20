import pytest
from account import Account


class TestAccountCreation:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678901"
        assert account.balance == 0.0

    @pytest.mark.parametrize("pesel", ["12345", "12345ABCDE1", "1234567890123", ""])
    def test_invalid_pesel(self, pesel):
        account = Account("Anna", "Nowak", pesel)
        assert account.pesel == "Invalid"

    @pytest.mark.parametrize("pesel, promo_code, expected_balance", [
        ("80010112345", "PROM_O10", 50.0),      
        ("80010112345", None, 0.0),            
        ("80010112345", "PROM_O10F", 0.0),     
        ("80010112345", None, 0.0),            
        ("52101012345", "PROM_O10", 0.0)      # invalid age
    ])
    def test_promo_code(self, pesel, promo_code, expected_balance):
        account = Account("Ewa", "Kowalska", pesel, promo_code=promo_code)
        assert account.balance == expected_balance

    def test_birth_year_calculation(self):
        account = Account("Marek", "Lewandowski", "44051401359")
        assert account.calculate_birth_year() == 1944