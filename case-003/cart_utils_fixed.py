def average_item_price(prices):
    if not prices:
        return 0.0
    total = 0
    for p in prices:
        total = total + p
    return total / len(prices)
