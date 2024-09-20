class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]+nums[i+1])
        return prefix