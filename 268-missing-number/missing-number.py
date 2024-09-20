class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        h={}
        a=len(arr)
        for ele in arr:
            if ele in h:
                h[ele]=True
            else:
                h[ele]=False
        for i in range(a+1):
            if i not in h:
                return i