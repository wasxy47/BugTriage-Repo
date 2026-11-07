from cart_utils import average_item_price


def test_average_item_price_100_200_300():
    assert average_item_price([100, 200, 300]) == 200.0


def test_average_item_price_50():
    assert average_item_price([50]) == 50.0


def test_average_item_price_10_20():
    assert average_item_price([10, 20]) == 15.0


def test_average_item_price_empty():
    assert average_item_price([]) == 0.0
