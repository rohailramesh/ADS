# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

'''
array[i] => price of stock on i th day
buy on day min(array[i])
sell on day max(array[i])
profit = sell - buy
must buy before you sell
'''

def stock_trading(array):
    if len(array) < 2:
        return 0 #no profit made since no of prices is less than 2
    min_profit = array[0]
    max_profit = 0
    
    for i in range(1,len(array)):
        current_profit = array[i] - min_profit #checking if we can sell on current day
        print(f'current profit = {current_profit}')
        max_profit = max(current_profit, max_profit)
        min_profit = min(min_profit, array[i])
    return max_profit
    
array = [7,1,5,3,6,4]
print(stock_trading(array))

# def stock_trading(prices):
#     # Edge case: If there are less than 2 prices, we cannot make a transaction
#     if len(prices) < 2:
#         return 0

#     min_price = prices[0]  # Initialize with the first day's price
#     max_profit = 0         # Initialize max profit to 0
    
#     # Traverse the prices array starting from the second day
#     for i in range(1, len(prices)):
#         # Check if we can make a profit by selling on the current day
#         current_profit = prices[i] - min_price
#         # Update max profit if the current profit is higher
#         max_profit = max(max_profit, current_profit)
#         # Update the min_price to the lowest we've seen so far
#         min_price = min(min_price, prices[i])
    
#     return max_profit
