from pymongo import MongoClient
from src.personal_account import PersonalAccount

class MongoAccountsRepository():
    def __init__(self, host="localhost", port=27017, db_name="bank_db", collection_name="accounts"):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_all(self, accounts):
        self.collection.delete_many({})
        
        if not accounts:
            return

        data = []
        for account in accounts:
            account_data = {
                "first_name": account.first_name,
                "last_name": account.last_name,
                "pesel": account.pesel,
                "balance": account.balance,
                "history": account.history
            }
            data.append(account_data)
        self.collection.insert_many(data)

    def load_all(self):
        accounts = []
        documents = self.collection.find()
        
        for doc in documents:
            acc = PersonalAccount(doc["first_name"], doc["last_name"], doc["pesel"])
            acc.balance = doc["balance"]
            acc.history = doc["history"]
            accounts.append(acc)
            
        return accounts