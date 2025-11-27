from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
def create_app():
    app = Flask(__name__)
    app.registry = AccountRegistry()
    app.config["TESTING"] = True 
    @app.route("/api/accounts", methods=['POST'])
    def create_account():
        data = request.get_json()
        print(f"Create account request: {data}")
        account = PersonalAccount(
            data["name"],
            data["surname"],
            data["pesel"],
            data.get("promocode")
        )
        app.registry.add_account(account)
        return jsonify({"message": "Account created"}), 201

    @app.route("/api/accounts", methods=['GET'])
    def get_all_accounts():
        print("Get all accounts request received")
        accounts = app.registry.get_all_accounts()
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

    @app.route("/api/accounts/count", methods=['GET'])
    def get_account_count():
        print("Get account count request received")
        accounts = app.registry.get_all_accounts()
        count = len(accounts)
        return jsonify({"count": count}), 200

    @app.route("/api/accounts/<pesel>", methods=['GET'])
    def get_account_by_pesel(pesel):
        account = app.registry.find_account_by_pesel(pesel)
        if account is None:
            return jsonify({"error": "Account not found"}), 404
        return jsonify({
            "name": account.first_name,
            "surname": account.last_name,
            "pesel": account.pesel,
            "balance": account.balance
        }), 200

    @app.route("/api/accounts/<pesel>", methods=['PATCH'])
    def update_account(pesel):
        account = app.registry.find_account_by_pesel(pesel)
        if account is None:
            return jsonify({"error": "Account not found"}), 404
        data = request.get_json()
        if "name" in data:
            account.first_name = data["name"]
        if "surname" in data:
            account.last_name = data["surname"]
        return jsonify({"message": "Account updated"}), 200

    @app.route("/api/accounts/<pesel>", methods=['DELETE'])
    def delete_account(pesel):
        account = app.registry.find_account_by_pesel(pesel)
        if account is None:
            return jsonify({"error": "Account not found"}), 404
        app.registry.remove_account(account)
        return jsonify({"message": "Account deleted"}), 200

    # ENDPOINT FOR TEST CLEANUP ##############################
    @app.route("/api/accounts/clear", methods=['POST'])
    def clear_accounts():
        if not app.config.get("TESTING", False):
            return jsonify({"error": "Not allowed"}), 403
        app.registry.accounts.clear()
        return jsonify({"message": "Registry cleared"}), 200
    #########################################################
    return app