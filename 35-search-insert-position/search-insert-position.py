from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Base case for empty list
        if len(nums) == 0:
            return 0
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If target is not found, return the insertion index
        return left



#do not operate on bs like this
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         mid=(len(nums)-1)//2
#         if len(nums)==0:
#             return 0
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]>target:
#             return self.searchInsert(nums[:mid], target)
#         else:
#             return self.searchInsert(nums[mid:], target)