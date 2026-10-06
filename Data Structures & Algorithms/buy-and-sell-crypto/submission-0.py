#imagine selling at each price (current price - lowest price seen so far)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 # for the best profit
        minBuy = prices[0] # set as the first price, continue iterating through
        for sell in prices: # loop through each price
            maxP = max(maxP, sell - minBuy) # update maxP with current price - lowest price
            minBuy = min(minBuy, sell) # updates minBuy if we find a smaller price
        return maxP
