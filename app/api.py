import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#flask --app app/api.py --debug run
from flask import Flask, app
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
from app.routes.accounts import accounts_bp
from src.mongo_accounts_repository import MongoAccountsRepository

def create_app():
    app = Flask(__name__)
    app.registry = AccountRegistry()
    app.accounts_repository = MongoAccountsRepository()
    app.config["TESTING"] = True 
    app.register_blueprint(accounts_bp)
    return app