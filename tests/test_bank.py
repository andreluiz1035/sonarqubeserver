import pytest
from src.app.bank import BankAccount


def test_deposit():
    acc = BankAccount("Andre", 100)
    assert acc.deposit(50) == 150


def test_withdraw():
    acc = BankAccount("Andre", 200)
    assert acc.withdraw(100) == 100


def test_withdraw_insufficient():
    acc = BankAccount("Andre", 50)
    with pytest.raises(ValueError):
        acc.withdraw(100)


def test_transfer():
    acc1 = BankAccount("A", 500)
    acc2 = BankAccount("B", 100)
    acc1.transfer(acc2, 200)
    assert acc1.balance == 300
    assert acc2.balance == 300