from account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe","12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678901"
        assert account.balance == 0.0
    def test_invalid_pesel_too_short(self):
        account = Account("Anna", "Nowak", "12345")
        assert account.pesel == "Invalid"
    def test_invalid_pesel_non_digit(self):
        account = Account("Jan", "Kowalski", "12345ABCDE1")
        assert account.pesel == "Invalid"
    def test_invalid_pesel_too_long(self):
        account = Account("Piotr", "Zielinski", "1234567890123")
        assert account.pesel == "Invalid"
    def test_valid_promo_code(self):
        account = Account("Ewa", "Kowalska", "12345678901", promo_code="PROM_O10")
        assert account.promo_code == "PROM_O10"
        assert account.balance == 50.0
    def test_invalid_promo_code(self):
        account = Account("Ewa", "Kowalska", "12345678901", promo_code="PROM_O10F")
        assert account.promo_code == None
        assert account.balance == 0.0
    def test_no_promo_code(self):
        account = Account("Ewa", "Kowalska", "12345678901")
        assert account.promo_code is None
        assert account.balance == 0.0
    def test_valid_age_promo_code(self):
        account = Account("Ewa", "Kowalska", "12345678901",promo_code="PROM_O10")
        assert account.promo_code is not None
        assert account.balance == 50.0
    def test_invalid_age_promo_code(self):
        account = Account("Ewa", "Kowalska", "52105678901",promo_code="PROM_O10")
        assert account.promo_code is None
        assert account.balance == 0.0
    def test_birth_year_calculation(self):
        account = Account("Marek", "Lewandowski", "44051401359")
        assert account.calculate_birth_year() == 1944