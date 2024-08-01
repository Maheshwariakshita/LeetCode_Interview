#3 one loop
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 
        if len(nums)==1:
            return nums[0]
        # if len(nums)==2:
        #     return max(nums[0], nums[1], nums[0]+nums[1])
        ans=nums[0]
        a=nums[0]
        for i in range(1,len(nums)):
            a=max(nums[i], a+nums[i])
            ans=max(a, ans)
        return ans



# 2 kadane,,,,,
# import sys
# class Solution:
#     def maxSubArray(self, arr: List[int]) -> int:
#         maxi = -sys.maxsize-1  # maximum sum
#         sum = 0
#         for num in arr:
#             sum += num
#             if sum > maxi:
#                 maxi = sum
#             if sum < 0:
#                 sum = 0
#         return maxi

# 1 two loops
# class Solution:
#     def maxSubArray(self, arr: List[int]) -> int:
#         if len(arr)==0:
#             return 0
#         if len(arr)==1:
#             return arr[0]
#         r=arr[0]
#         for i in range(len(arr)):
#             a=0
#             for j in range(i, len(arr)):
#                 a=arr[j]+a
#                 r=max(a, r)
#         return r
