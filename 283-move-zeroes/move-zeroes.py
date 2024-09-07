class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # pointer for non-zero elements

        # Move all non-zero elements to the front
        for j in range(len(arr)):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]  # Swap non-zero element with the element at index i
                i += 1

        # #here time limit exceeded
        # i=0
        # j=i+1
        # while i<len(arr) and j<len(arr):
        #     if i==0 and j!=0:
        #         arr[i], arr[j]=arr[j], arr[i]
        #         i+=1
        #         j+=1
        #     elif j==0:
        #         j+=1




        #did not worked
        # i=0
        # j=len(nums)-1
        # while i<=j:
        #     if nums[i]==0:
        #         nums[i], nums[j]=nums[j], nums[i]
        #         j-=1
        #     else:
        #         i+=1






        # lastNonZeroFoundAt = 0
        
        # for cur in range(len(nums)):
        #     if nums[cur] != 0:
        #         nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
        #         lastNonZeroFoundAt += 1
