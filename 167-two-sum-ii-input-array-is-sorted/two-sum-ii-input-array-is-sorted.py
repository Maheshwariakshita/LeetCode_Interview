class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]<=target:
                i+=1
            else: 
                j-=1
        
        # 2
        # num_to_index = {}
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in num_to_index:
        #         return [num_to_index[complement] + 1, i + 1]
        #     num_to_index[num] = i
        
        
        
        
        
        
        
        
        
        #        #two pointer
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     a=nums[i]+nums[j]
        #     if a==target:
        #         return [i+1, j+1]
        #     elif a<target:
        #         i+=1
        #     else:
        #         j-=1
        # return
