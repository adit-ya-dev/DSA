"Given prices array, find maximum profit by buying once and selling once.

Example
Input: prices = [7,1,5,3,6,4]
Output: 5 "

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit
