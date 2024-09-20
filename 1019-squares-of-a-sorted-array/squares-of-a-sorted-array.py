import math
class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i]=pow(arr[i],2)
        a=[0]*len(arr)
        pos=len(arr)-1
        
        i=0
        j=len(arr)-1
        while i<=j:
            if arr[i]<=arr[j]:
                a[pos]=arr[j]
                j-=1
                
            else:
                a[pos]=arr[i]
                i+=1
            pos-=1
                
        return a