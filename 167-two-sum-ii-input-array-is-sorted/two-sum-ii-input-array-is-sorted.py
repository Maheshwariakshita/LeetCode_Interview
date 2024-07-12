class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]<=target:
                i+=1
            else: 
                j-=1
        
        
        
        
        
        
        
        
        
        
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
