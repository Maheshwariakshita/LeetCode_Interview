class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         mini=0
#         maxi=mini
#         for i in range(len(prices)): 
#             for j in range(len(prices)):
#                 if prices[i]<prices[j]:
#                     mini=i #now we have index mini num
        
#         for k in range(mini+1, len(prices)):
#             for l in range(mini+1, len(prices)):
#                 if prices[k]>prices[l]:
#                     maxi=k
#         return prices[maxi]-prices[mini]
        
        