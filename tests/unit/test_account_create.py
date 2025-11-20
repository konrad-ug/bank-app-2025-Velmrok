import pytest
from personal_account import PersonalAccount


class TestAccountCreation:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678901"
        assert account.balance == 0.0

    @pytest.mark.parametrize("pesel", ["12345", "12345ABCDE1", "1234567890123", ""])
    def test_invalid_pesel(self, pesel):
        account = PersonalAccount("Anna", "Nowak", pesel)
        assert account.pesel == "Invalid"
    def test_valid_pesel(self):
        account = PersonalAccount("Anna", "Nowak", "80010112345")
        assert account.pesel == "80010112345"

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
    @pytest.mark.parametrize("history,should_succeed", [([100, 200, 150], True), ([100, -50, 200], False)])
    def test_recent_history(self, history, should_succeed):
        account = PersonalAccount("Test", "User", "80010112345")
        account.history = history
        assert account.has_positive_recent_history() is should_succeed
  
    @pytest.mark.parametrize("history,amount,should_succeed", [
        ([100, 200, 200, 300, 400], 1000, True),
        ([100, 100, 100, 100, 100], 600, False)
    ])
    def test_five_payments_exceeding_amount(self, history, amount, should_succeed):
        account = PersonalAccount("Test", "User", "80010112345")
        account.history = history
        assert account.has_five_payments_exceeding_amount(amount) is should_succeed
