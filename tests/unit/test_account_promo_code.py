import pytest
from src.personal_account import PersonalAccount

class TestAccountPromoCode:
    @pytest.mark.parametrize("pesel, promo_code, expected_balance", [
    ("80010112345", "PROM_O10", 50.0),      
    ("80010112345", None, 0.0),            
    ("80010112345", "PROM_O10F", 0.0),     
    ("80010112345", None, 0.0),            
    ("52101012345", "PROM_O10", 0.0)      # invalid age
])
    def test_promo_code(self, pesel, promo_code, expected_balance):
        account = PersonalAccount("Ewa", "Kowalska", pesel, promo_code=promo_code)
        assert account.balance == expected_balance
    def test_promo_code_with_invalid_pesel(self):
        account = PersonalAccount("Ewa", "Kowalska", "invalid_pesel", promo_code="PROM_ABC")
        assert account.balance == 0.0
        assert account.promo_code is None
    @pytest.mark.parametrize("pesel,expected_year", [("44051401359", 1944), ("01210112345", 2001), ("123", None)])
    def test_birth_year_calculation(self, pesel, expected_year):
        account = PersonalAccount("Marek", "Lewandowski", pesel)
        assert account.calculate_birth_year() == expected_year