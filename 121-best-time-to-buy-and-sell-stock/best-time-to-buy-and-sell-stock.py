class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Keep track of the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the profit if we sell at the current price
            profit = price - min_price
            # Update max_profit if the current profit is higher
            max_profit = max(max_profit, profit)

        return max_profit


# # time limit exceeded
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         curr=0
#         maxi=0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 curr=prices[j]-prices[i]
#                 maxi=max(maxi,curr )
#         return maxi







        # # 1 bf..with two loop
        # ans=0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         ans=max(ans, prices[j]-prices[i])
        # return ans

        # 2.. pointer or sliding window... one loop

        # mini=prices[0]
        # ans=0
        # for i in range(len(prices)):
        #     mini=min(mini, prices[i])
        #     ans=max(ans, prices[i]-mini) 
        # return ans