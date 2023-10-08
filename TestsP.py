import pytest
from Gui import *


#
# def start_game(count: int):
#     try:
#         if count >= 5:
#             return True
#         else:
#             return False
#     except Exception as e:
#         print("you losed")
#         return None
#
# def PasswordsDisplay(x : str):
#     try:
#         if x == '':
#             return False
#         else:
#             with open(x, "r") as file:
#                 text = file.read()
#             return text
#     except Exception as e:
#         return None
#

def test_start_game():
    assert start_game(5) == True
    assert start_game(4) == False
    assert start_game(0) == None
    assert start_game(None) == None


def test_PasswordsDisplay():
    assert PasswordsDisplay('user.txt') == 'aaa'
    assert PasswordsDisplay('') == False
    assert PasswordsDisplay(None) == None
