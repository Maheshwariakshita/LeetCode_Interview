class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
               
       
       
       
       
       
        # #two pointer
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [i, j]
        #     i+=1
        #     j-=1
        # return






# class Solution:

#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         h={}

#         for i, j in enumerate(nums):
#             diff=target-j
#             if diff in h:
#                 return [j, h[j]]
#             else:
#                 h[j]=i



# class Solution:

#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         for i in range (len(a)):
#             for j in range (i+1,len(a)):
#                 if a[i]+a[j]==sum:
#                     if(a[i]<a[j]):
#                         print(a[i]," ",a[j])
#                     else:
#                         print(a[j]," ",a[i])













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