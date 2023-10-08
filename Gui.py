import pytest

def start_game(count: int):
    try:
        if count >= 5:
            return True
        else:
            return False
    except Exception as e:
        print("you losed")
        return None

def PasswordsDisplay(x : str):
    try:
        if x == '':
            return False
        else:
            with open(x, "r") as file:
                text = file.read()
            return text
    except Exception as e:
        return None
