import pytest
from src.app.order import Order


def test_total():
    order = Order([("Notebook", 1000, 1), ("Mouse", 50, 2)])
    assert order.total() == 1100


def test_discount():
    order = Order([("Notebook", 1000, 1)])
    assert order.apply_discount(10) == 900


def test_invalid_discount():
    order = Order([("Notebook", 1000, 1)])
    with pytest.raises(ValueError):
        order.apply_discount(150)


def test_free_shipping():
    order = Order([("TV", 300, 1)])
    assert order.has_free_shipping() is True