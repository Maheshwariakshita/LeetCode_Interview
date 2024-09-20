from typing import List

class Solution:
    def minStartValue(self, arr: List[int]) -> int:
        total_sum = 0
        min_sum = 0
        
        for num in arr:
            total_sum += num
            min_sum = min(min_sum, total_sum)
        
        # The minimum start value needed is 1 - min_sum
        # to ensure that the cumulative sum is always >= 1
        return 1 - min_sum
