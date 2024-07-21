# class Solution:

#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # 2 hashmap
#         h={}
#         for i, curr in enumerate(nums):     # {0:2, 1:7, 2:11, 3:15}
#             diff=target-curr
#             if diff in h:
#                 return [i, h[diff]]
#             h[curr]=i

#     # h={2:0, 7:1, ......} h[curr]=i


        # 1 brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
   
       

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x:x[1])
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l][1]+nums[r][1] == target:
                return sorted([nums[l][0], nums[r][0]])
            elif nums[l][1]+nums[r][1] < target:
                l += 1
            else:
                r -= 1
        return 