import pytest
from src.personal_account import PersonalAccount


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

   
    
