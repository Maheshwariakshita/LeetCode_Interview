class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if not nums:
            return 0
        if len(nums)<k:
            return 0
        maxi_s=sum(nums[:k])
        curr_s=maxi_s
        n=len(nums)
        for i in range(k,n):
            curr_s+=nums[i]-nums[i-k]
            maxi_s=max(maxi_s, curr_s)
        return maxi_s/k








        # if not nums:
        #     return 0
        # if len(nums) < k:
        #     return 0
        
        # n = len(nums)
        # max_sum = sum(nums[:k])  
        # current_sum = max_sum
        
        # for i in range(k, n):
        #     current_sum += nums[i] - nums[i - k]  
        #     max_sum = max(max_sum, current_sum)  
        # return max_sum / k 
