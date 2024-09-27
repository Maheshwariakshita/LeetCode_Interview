class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n=len(arr)
        prefix=[arr[0]]
        for i in range(1,n):
            prefix.append(arr[i]+prefix[-1])
        return prefix
        












        # prefix=[nums[0]]
        # for i in range(len(nums)-1):
        #     prefix.append(prefix[-1]+nums[i+1])
        # return prefix