class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 diff maximum via loop
        #2 pointer approach 0, len-1-> 
        #3 max, min- diff 

        # # 1 bf
        # ans=0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         ans=max(ans, prices[j]-prices[i])
        # return ans

        # 2 with dp

        mini=prices[0]
        ans=0
        for i in range(len(prices)):
            mini=min(mini, prices[i])
            ans=max(ans, prices[i]-mini) 
        return ans