from company_account import CompanyAccount

class TestCompanyAccount:
    def test_create_company_account(self):
        account = CompanyAccount("Test Company", "1234567890")
        assert account.company_name == "Test Company"
        assert account.nip == "1234567890"
        assert account.validate_nip() == True
    def test_invalid_nip_length(self):
        account = CompanyAccount("Test Company", "12345")
        assert account.nip == "Invalid"
        assert account.validate_nip() == False
    def test_invalid_nip_non_digit(self):
        account = CompanyAccount("Test Company", "12345ABCDE")
        assert account.nip == "Invalid"
        assert account.validate_nip() == False