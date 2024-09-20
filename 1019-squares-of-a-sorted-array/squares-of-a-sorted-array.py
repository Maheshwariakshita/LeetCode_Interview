import math
class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i]=pow(arr[i],2)
        # i=0
        # j=len(arr)-1
        # while i<=j:
        #     if arr[i]<=arr[j]:
        #         i+=1
        #         j-=1
        #     else:
        #         arr[i], arr[j]=arr[j], arr[i]
        #         i+=1
        #         j-=1
        return sorted(arr)