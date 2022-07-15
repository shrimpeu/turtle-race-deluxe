import bcrypt
import json
import os


USER_DATA_FILE = f"{os.path.dirname(__file__)}/user_data.json"


if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "r") as data:
        EXISTING_ACCOUNTS = json.load(data)


def hash_str(s: str) -> str:
    return bcrypt.hashpw(s, bcrypt.gensalt()).decode("utf-8").replace("'", '"')


def write_json(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4, separators=(",", ": "), sort_keys=True)


def email_taken(input_email: str) -> bool:
    for existing_email in EXISTING_ACCOUNTS:
        existing_email = existing_email.encode("utf-8")
        if bcrypt.checkpw(input_email, existing_email):
            return True
    return False


def get_existing_email(input_email: str) -> str:
    for existing_email in EXISTING_ACCOUNTS:
        existing_email = existing_email.encode("utf-8")
        if bcrypt.checkpw(input_email, existing_email):
            return existing_email.decode("utf-8").replace("'", '"')

def update_balance(email: str, new_balance: int) -> None:
    print(email)
    print(new_balance)
    with open("user_data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data[email]["balance"] = new_balance

    with open("user_data.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4, separators=(",", ": "), sort_keys=True)