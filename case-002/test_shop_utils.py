import pytest

from shop_utils import apply_discount


def test_apply_discount_200_10():
    assert apply_discount(200, 10) == 180.0


def test_apply_discount_100_0():
    assert apply_discount(100, 0) == 100.0


def test_apply_discount_100_100():
    assert apply_discount(100, 100) == 0.0


def test_apply_discount_49_99_20():
    assert apply_discount(49.99, 20) == pytest.approx(39.992)


def test_apply_discount_10000_25():
    assert apply_discount(10000, 25) == 7500.0
