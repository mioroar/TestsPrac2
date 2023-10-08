import pytest
from Gui import *


def test_start_game():
    assert start_game(5) == False
    assert start_game(4) == False
    assert start_game(0) == False
    assert start_game(None) is False


def test_PasswordsDisplay():
    assert PasswordsDisplay('user.txt') == 'aaa'
    assert PasswordsDisplay('') == False
    assert PasswordsDisplay(None) == None
