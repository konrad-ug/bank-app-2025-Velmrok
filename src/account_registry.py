
class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if account is None:
            raise ValueError("Cannot add a null account.")
        for acc in self.accounts:
            if acc.pesel == account.pesel:
                raise ValueError(f"Account with PESEL {account.pesel} already exists.")
        self.accounts.append(account)
    def find_account_by_pesel(self, pesel):
        if not pesel or len(str(pesel)) != 11 or not str(pesel).isdigit():
            return None
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
    def get_all_accounts(self):
        return self.accounts.copy()
    def get_count(self):
        return len(self.accounts)
    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)

    