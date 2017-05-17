import sys
def find_max_profit(prices):
    if prices is None:
        return ('prices cannot be None')
    if len(prices) < 2:
        return ('prices must have at least two values')
    min_price = prices[0]
    max_profit = -sys.maxsize
    for index, price in enumerate(prices):
        if index == 0:
            continue
        profit = price - min_price
        min_price = min(price, min_price)
        max_profit = max(profit, max_profit)
    return max_profit
b = [8, 5, 3, 2, 1]
print(find_max_profit(b))