from behave import *
import requests

URL = "http://127.0.0.1:5000"

@step('Account with pesel "{pesel}" has balance: "{balance}"')
def set_account_balance(context, pesel, balance):
    json_body = {
        "amount": int(balance),
        "type": "incoming"
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    assert response.status_code == 200, f"Failed to set balance: {response.text}"

@when('I transfer "{amount}" from account "{from_pesel}" to account "{to_pesel}"')
def transfer_money(context, amount, from_pesel, to_pesel):
    json_body_out = {
        "amount": int(amount),
        "type": "outgoing"
    }
    response_out = requests.post(URL + f"/api/accounts/{from_pesel}/transfer", json=json_body_out)
    context.last_transfer_response = response_out 

    if response_out.status_code != 200:
        return

    json_body_in = {
        "amount": int(amount),
        "type": "incoming"
    }
    response_in = requests.post(URL + f"/api/accounts/{to_pesel}/transfer", json=json_body_in)
    assert response_in.status_code == 200, f"Incoming transfer failed: {response_in.text}"

@when('I attempt to transfer "{amount}" from account "{from_pesel}" to account "{to_pesel}"')
def attempt_transfer_money(context, amount, from_pesel, to_pesel):
    json_body = {
        "amount": int(amount),
        "type": "outgoing"
    }
    response = requests.post(URL + f"/api/accounts/{from_pesel}/transfer", json=json_body)
    context.last_transfer_response = response

@then('Transfer should fail with error "{error_message}"')
def check_transfer_error(context, error_message):
    assert context.last_transfer_response.status_code in [400, 404, 422], \
        f"Expected error status code, got {context.last_transfer_response.status_code}"
    
    response_json = context.last_transfer_response.json()
    received_error = response_json.get("error", "")
 
    assert error_message in received_error, \
        f"Expected error message containing '{error_message}', got '{received_error}'"

@when('I make express transfer of "{amount}" from account "{pesel}"')
def express_transfer(context, amount, pesel):
    json_body = {
        "amount": int(amount),
        "type": "express"
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_transfer_response = response
    assert response.status_code == 200, f"Express transfer failed: {response.text}"