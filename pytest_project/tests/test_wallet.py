# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest
from pytest_project.wallet import Wallet, InsufficientAmount



# Individuele tests
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)



# tests met fixtures om herhaling te vermijden.
# @pytest.fixture decorator gebruiken om fixtures aan te maken
# gebruik ''' ''' om comments toe te voegen die vermeld worden wanneer $ pytest --fixtures ingegeven wordt
@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)



# Parametrized test functions
# Kan gebruikt worden om combinaties van methodes te testen 
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected



# combinatie van fixtures en parametrized test functions
@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected