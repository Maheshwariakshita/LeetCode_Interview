class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """

        n = len(nums)
        k %= n  # In case k is greater than the length of the array

        # Step 1: Reverse the entire array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining n - k elements
        nums[k:] = reversed(nums[k:])

        #tle
        # for i in range(k):
        #     temp=nums[-1]
            
        #     for j in range(len(nums)-1,0,-1):
        #         nums[j], nums[j-1]=nums[j-1], nums[j]
        #     nums[0]=temp
        # for j in range(k):
        #     temp=nums[0]
            
        #     for i in range(len(nums)-1):
        #         nums[i], nums[i+1]=nums[i+1], nums[i]
        #     nums[-1]=temp