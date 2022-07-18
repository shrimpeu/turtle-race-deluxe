import bcrypt
import json
import os
import re

from tkinter import messagebox


USER_DATA_FILE = f"{os.path.dirname(__file__)}/user_data.json"

# Initiate user database
if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "r") as data:
        EXISTING_ACCOUNTS = json.load(data)
else:
    sample_account = {
        "$2b$12$BcqOABIQYslBPyCE3c9l9ewjVjG39J/X.x3cfK6LNW/OJY0UlnY2C": {
            "balance": 0,
            "first_name": "Sample",
            "last_name": "Account",
            "pword": "$2b$12$VvNB/klBN8BOdYoTtoBIl.nb4.TMK6Pwnhlf7SwPM323diEcoSRx2"}
    }
    with open(USER_DATA_FILE, "w") as f:
        json.dump(sample_account, f, indent=4, separators=(",", ": "), sort_keys=True)
    with open(USER_DATA_FILE, "r") as data:
        EXISTING_ACCOUNTS = json.load(data)


def hash_str(s: str) -> str:
    return bcrypt.hashpw(s, bcrypt.gensalt()).decode("utf-8").replace("'", '"')


def write_json(data) -> None:
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


def add_new_account(email: str, first_name: str, last_name: str, passwd: str) -> None:
    passwd = hash_str(passwd.encode("utf-8"))

    EXISTING_ACCOUNTS[email] = {
            "first_name": first_name,
            "last_name": last_name,
            "pword": passwd,
            "balance": 0
            }
    write_json(EXISTING_ACCOUNTS)

    messagebox.showinfo(title="Account Created", message="Account successfully created!")    


def update_balance(email: str, new_balance: int) -> None:
    with open("user_data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data[email]["balance"] = new_balance

    write_json(data)


def input_not_empty(root: type, entries: tuple) -> bool:
    for e in entries:
        if len(e) == 0:
            messagebox.showwarning(title="Invalid Input", message="Empty Input!")
            root.lift()
            return False
    return True


def valid_amount(root: type, method: str, input_amount: int, current_bal: int) -> bool:
    if method == "withdraw":
        if input_amount >= 300 and current_bal >= 300:
            return True
        else:
            messagebox.showwarning(title="Invalid Input", message="Insufficient Balance / Amount input is below minimum.")
            root.lift()
            return False
    else:
        if input_amount >= 100:
            return True
        else:
            messagebox.showwarning(title="Invalid Input", message="Insufficient Balance / Amount input is below minimum.")
            root.lift()
            return False


def curr_balance(email: str) -> int:
    with open(USER_DATA_FILE, "r") as f:
        data = json.load(f)
    return data[email]["balance"]


def valid_passwd(root: type, passwd: str) -> bool:
    if len(passwd) >= 8:
        return True
    messagebox.showwarning(
        title="Invalid Input",
        message="Password must be 8 characters long or more."
    )
    root.lift()
    return False


def valid_email(root:type , email: str) -> bool:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    messagebox.showwarning(title="Invalid Input", message="Invalid Email.")
    root.lift()
    return False


def display_result(winners: str, bets_won: int) -> str:
    result = f"""
    WINNER: {winners}
    TOTAL WINS: Php {bets_won}
    """

    return result