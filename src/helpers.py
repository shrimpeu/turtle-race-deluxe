import bcrypt
import json
import getpass
import os
import re

from tkinter import messagebox

USER_NAME = getpass.getuser()
if os.name == "nt":
    USER_DATA_PATH = f"C:\\Users\\{USER_NAME}\\AppData\\Local\\TRDeluxe"
    USER_DATA_FILE = f"{USER_DATA_PATH}\\user_data.json"
else:
    USER_DATA_PATH = f"/home/{USER_NAME}/.local/share/TRDeluxe"
    USER_DATA_FILE = f"{USER_DATA_PATH}/user_data.json"

if not os.path.exists(USER_DATA_PATH):
    os.makedirs(USER_DATA_PATH)


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


def hash_str(s: bytes) -> str:
    """Encrypts the string with `bcrypt` module"""
    return bcrypt.hashpw(s, bcrypt.gensalt()).decode("utf-8").replace("'", '"')


def write_json(data: dict) -> None:
    """Writes the data in user database"""
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4, separators=(",", ": "), sort_keys=True)


def email_taken(input_email: bytes) -> bool:
    """Returns `True` if `input_email` is already in user database"""
    for existing_email in EXISTING_ACCOUNTS:
        existing_email = existing_email.encode("utf-8")
        if bcrypt.checkpw(input_email, existing_email):
            return True
    return False


def get_existing_email(input_email: bytes) -> None:
    """Returns the email from the user database that matched with `input_email`"""
    for existing_email in EXISTING_ACCOUNTS:
        existing_email = existing_email.encode("utf-8")
        if bcrypt.checkpw(input_email, existing_email):
            return existing_email.decode("utf-8").replace("'", '"')


def add_new_account(email: str, first_name: str, last_name: str, passwd: str) -> None:
    """Stores new account in user database"""
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
    """Write to user database the new balance"""
    with open(USER_DATA_FILE, "r") as jsonFile:
        data = json.load(jsonFile)

    data[email]["balance"] = new_balance

    write_json(data)


def input_not_empty(root, entries: list[str]) -> bool:
    """Returns `True` if elements in entries are not empty"""
    for e in entries:
        if len(e) == 0:
            messagebox.showwarning(title="Invalid Input", message="Empty Input!")
            root.lift()
            return False
    return True


def valid_amount(root, method: str, input_amount: int, current_bal: int) -> bool:
    """Returns `True` if `input_amount` is valid based on method and current balance"""
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
    """Returns the balance currently stored in user database"""
    with open(USER_DATA_FILE, "r") as f:
        data = json.load(f)
    return data[email]["balance"]


def valid_passwd(root, passwd: str) -> bool:
    """Returns `True` if password length in 8 or more"""
    if len(passwd) >= 8:
        return True
    messagebox.showwarning(
        title="Invalid Input",
        message="Password must be 8 characters long or more."
    )
    root.lift()
    return False


def valid_email(root, email: str) -> bool:
    """Returns `True` if the email pattern is valid"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    messagebox.showwarning(title="Invalid Input", message="Invalid Email.")
    root.lift()
    return False


def display_result(winners: str, bets_won: int) -> str:
    """Returns the formatted string for displaying the game result"""
    result = f"""
    WINNER: {winners}
    TOTAL WINS: Php {bets_won}
    """

    return result
