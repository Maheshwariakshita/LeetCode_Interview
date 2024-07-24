import sys
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxi = -sys.maxsize-1  # maximum sum
        sum = 0
        for num in arr:
            sum += num
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi


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
