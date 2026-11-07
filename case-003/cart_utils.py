def average_item_price(prices):
    total = 0
    for p in prices:
        total = total + p
    return total / len(prices)
