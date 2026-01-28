import pytest
import mongomock
from src.mongo_accounts_repository import MongoAccountsRepository
from src.personal_account import PersonalAccount
from unittest.mock import patch
@pytest.fixture
def mock_mongo():
    with patch('src.mongo_accounts_repository.MongoClient', new=mongomock.MongoClient):
        yield

def test_save_all_data_in_db(mock_mongo):
    repo = MongoAccountsRepository()
    account = PersonalAccount("Janusz", "Biznesu", "12345678901")
    account.balance = 500.0
    account.history = [100.0, 400.0]
    repo.save_all([account])

    saved_doc = repo.collection.find_one({"pesel": "12345678901"})    
    assert saved_doc is not None
    assert saved_doc["first_name"] == "Janusz"
    assert saved_doc["balance"] == 500.0
    assert saved_doc["history"] == [100.0, 400.0]

def test_load_all_data_from_db(mock_mongo):
    repo = MongoAccountsRepository()
    repo.collection.insert_one({
        "first_name": "Grażyna",
        "last_name": "Testowa",
        "pesel": "98765432101",
        "balance": 200.0,
        "history": [50.0]
    })
    loaded_accounts = repo.load_all()

    assert len(loaded_accounts) == 1
    acc = loaded_accounts[0]
    assert isinstance(acc, PersonalAccount)
    assert acc.first_name == "Grażyna"
    assert acc.pesel == "98765432101"
    assert acc.balance == 200.0
    assert acc.history == [50.0]

def test_save_all_clears_collection_before_saving(mock_mongo):

    repo = MongoAccountsRepository()
    repo.collection.insert_one({"first_name": "Stary", "pesel": "00000000000"})
    new_account = PersonalAccount("Nowy", "Konto", "11111111111")
    repo.save_all([new_account])


    docs = list(repo.collection.find())
    assert len(docs) == 1
    assert docs[0]["first_name"] == "Nowy"

def test_save_all_with_empty_list_clears_collection(mock_mongo):
    repo = MongoAccountsRepository()
    repo.collection.insert_one({"first_name": "DoUsuniecia", "pesel": "22222222222"})
    repo.save_all([])

    docs = list(repo.collection.find())
    assert len(docs) == 0
    