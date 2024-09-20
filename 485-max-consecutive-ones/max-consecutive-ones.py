class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        if len(arr)==0:
            return 0
        if len(arr)==1:
            if arr[0]==1:
                return 1
            else:
                return 0
        # prev=float('-inf')
        max_c=0
        curr_c=0
        
        for ele in arr:
            if ele==1 :
                curr_c+=1
            else:
                curr_c=0
            max_c=max(max_c, curr_c)
            
        return max_c