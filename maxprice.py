def maxProfit(prices):
    if(len(prices) == 0):
        return 0
    maxvalue = 0
    low = prices[0]
    for price in prices:
        low = min(price,low)
        maxvalue = max(price - low,maxvalue)
    return maxvalue

print maxProfit([3,2,3,1,2])