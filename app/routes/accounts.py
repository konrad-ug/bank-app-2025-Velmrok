

from flask import Blueprint, app, request, jsonify, current_app
from src.personal_account import PersonalAccount

accounts_bp = Blueprint('accounts', __name__,url_prefix='/api/accounts')


@accounts_bp.route("", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(
        data["name"],
        data["surname"],
        data["pesel"],
        data.get("promocode")
    )
    if(current_app.registry.find_account_by_pesel(account.pesel) is not None):
        return jsonify({"error": "Account with this PESEL already exists"}), 409
    current_app.registry.add_account(account)
    return jsonify({"message": "Account created"}), 201

@accounts_bp.route("", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = current_app.registry.get_all_accounts()
    accounts_data = [
        {
            "name": acc.first_name,
            "surname": acc.last_name,
            "pesel": acc.pesel,
            "balance": acc.balance
        }
        for acc in accounts
    ]
    return jsonify(accounts_data), 200

@accounts_bp.route("/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    accounts = current_app.registry.get_all_accounts()
    count = len(accounts)
    return jsonify({"count": count}), 200

@accounts_bp.route("<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    account = current_app.registry.find_account_by_pesel(pesel)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify({
        "name": account.first_name,
        "surname": account.last_name,
        "pesel": account.pesel,
        "balance": account.balance
    }), 200

@accounts_bp.route("<pesel>", methods=['PATCH'])
def update_account(pesel):
    account = current_app.registry.find_account_by_pesel(pesel)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    data = request.get_json()
    if "name" in data:
        account.first_name = data["name"]
    if "surname" in data:
        account.last_name = data["surname"]
    return jsonify({"message": "Account updated"}), 200

@accounts_bp.route("<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = current_app.registry.find_account_by_pesel(pesel)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    current_app.registry.remove_account(account)
    return jsonify({"message": "Account deleted"}), 200
@accounts_bp.route("<pesel>/transfer", methods=['POST'])
def transfer(pesel):
    account = current_app.registry.find_account_by_pesel(pesel)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    data = request.get_json()
    amount = data.get("amount")
    type = data.get("type")
    if type not in ["incoming", "outgoing","express"]:
        return jsonify({"error": "Invalid transfer type", "balance": account.balance}),400
    if amount is None or not isinstance(amount, (int, float)):
        return jsonify({"error": "Invalid amount", "balance": account.balance}), 422
    if type == "outgoing" :
        try:
            account.withdraw(amount)
        except ValueError as e:
            return jsonify({"error": str(e), "balance": account.balance}), 422
    elif type == "incoming":
        try:
            account.deposit(amount)
        except ValueError as e:
            return jsonify({"error": str(e), "balance": account.balance}), 422
    elif type == "express": 
        try:
            account.express_withdraw(amount)
        except ValueError as e:
            return jsonify({"error": str(e), "balance": account.balance}), 422
    return jsonify({"message": "Transfer successful", "balance": account.balance}), 200

@accounts_bp.route("/save", methods=['POST'])
def save_registry():
    print("Registry saved to database")
    accounts = current_app.registry.get_all_accounts()
    current_app.accounts_repository.save_all(accounts)
    return jsonify({"message": "Registry saved to database"}), 200

@accounts_bp.route("/load", methods=['POST'])
def load_registry():
    print("Registry loaded from database")
    current_app.registry.clear_accounts()
    loaded_accounts = current_app.accounts_repository.load_all()
    for acc in loaded_accounts:
        current_app.registry.add_account(acc)
    return jsonify({"message": "Registry loaded from database"}), 200


# ENDPOINT FOR TEST CLEANUP ##############################
@accounts_bp.route("clear", methods=['POST'])
def clear_accounts():
    if not current_app.config.get("TESTING", False):
        return jsonify({"error": "Not allowed"}), 403
    current_app.registry.accounts.clear()
    return jsonify({"message": "Registry cleared"}), 200
#########################################################