from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
from unittest.mock import patch
from datetime import date
import pytest

class TestAccountSendEmail:

    @pytest.fixture
    def personal_account(self):
        acc = PersonalAccount("John", "Doe", "12345678901")
        acc.history = [100.0, -20.0, 50.0]
        return acc

    @pytest.fixture
    def company_account(self):
        acc = CompanyAccount("Acme Corp", "1234567890")
        acc.history = [500.0, -100.0, 200.0]
        return acc

    @patch('src.smtp.smptp.SMTPClient.send')
    def test_send_history_personal_account_success(self, mock_send, personal_account):
        mock_send.return_value = True
        email = "test@example.com"
        result = personal_account.send_history_via_email(email)
        assert result is True
        
        expected_subject = f"Account Transfer History {date.today().isoformat()}"
        expected_text = f"Personal account history: {personal_account.history}"
        mock_send.assert_called_once_with(expected_subject, expected_text, email)

    @patch('src.smtp.smptp.SMTPClient.send')
    def test_send_history_company_account_success(self, mock_send, company_account):
        mock_send.return_value = True
        email = "company@example.com"
        result = company_account.send_history_via_email(email)
        assert result is True
        
        expected_subject = f"Account Transfer History {date.today().isoformat()}"
        expected_text = f"Company account history: {company_account.history}"
        
        mock_send.assert_called_once_with(expected_subject, expected_text, email)

    @patch('src.smtp.smptp.SMTPClient.send')
    def test_send_history_personal_account_failure(self, mock_send, personal_account):
        mock_send.return_value = False
        email = "fail@example.com"
        result = personal_account.send_history_via_email(email)
        assert result is False
        mock_send.assert_called_once() 

    @patch('src.smtp.smptp.SMTPClient.send')
    def test_send_history_company_account_failure(self, mock_send, company_account):
        mock_send.return_value = False
        email = "fail@example.com"
        result = company_account.send_history_via_email(email)
        assert result is False
        mock_send.assert_called_once()