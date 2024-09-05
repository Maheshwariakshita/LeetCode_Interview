class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        m=0
        e=len(nums)-1
        while m<=e:
            if  nums[m]==0:
                nums[s], nums[m]=nums[m], nums[s]
                s+=1
                m+=1
            elif nums[m]==1:
                m+=1
            elif nums[m]==2:
                nums[e], nums[m]=nums[m], nums[e] 
                e-=1
                







        # l,m,r=0,0,len(nums)-1
        # while m<=r:
        #     if nums[m]==0:
        #         nums[m], nums[l]=nums[l], nums[m]
        #         l+=1
        #         m+=1
        #     elif nums[m]==1:
        #         m+=1
        #     else:
        #         nums[m], nums[r]=nums[r], nums[m]
        #         r-=1
        
