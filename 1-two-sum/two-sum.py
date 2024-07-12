class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1
        # i=0
        # j=len(nums)-1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
               
       
       
       
       
        # 2
        h = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return [h[diff], i]  # Correct order of indices
            else:
                h[num] = i  # Store the index as the value
        return []















# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = enumerate(nums)
#         nums = sorted(nums, key=lambda x:x[1])
#         l, r = 0, len(nums)-1
#         while l < r:
#             if nums[l][1]+nums[r][1] == target:
#                 return sorted([nums[l][0], nums[r][0]])
#             elif nums[l][1]+nums[r][1] < target:
#                 l += 1
#             else:
#                 r -= 1
#         return 