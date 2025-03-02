import json

CREDENTIAL_FILE = "configurations/credentials.json"

def save_credentials(email, password):
    with open(CREDENTIAL_FILE, 'w') as file:
        json.dump({"email":email, "password":password}, file)

def load_credentials():
    with open(CREDENTIAL_FILE, 'r') as file:
        return json.load(file)

def get_address_details():
    with open("test_data/address_details.json", 'r') as file:
        return json.load(file)

def get_expected_saved_address():
    with open("test_data/expected_saved_address.json", 'r') as file:
        return json.load(file)