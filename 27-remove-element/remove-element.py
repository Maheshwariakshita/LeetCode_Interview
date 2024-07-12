class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        i = 0
        for j in range(len(arr)):
            if arr[j] != val:
                arr[i] = arr[j]
                i += 1
        return i
        # i=0
        # j=len(arr)-1
        # x=1
        # if len(arr)==0:
        #     return 
        # if len(arr)==1:
        #     if arr[0]==val:
        #         return 
        #     else:
        #         return 1

        # while i<=j:
        #     if arr[i]==val and arr[j]!=val:
        #         arr[i], arr[j]=arr[j], arr[i]
        #         i+=1
        #         j-=1
        #         x+=1
        #     elif arr[i]!=val and arr[j]!=val:
        #         i+=1
        #     elif arr[i]!=val and arr[j]==val:
        #         j-=1
        #         i+=1
        #     elif arr[i]==val and arr[j]==val:
        #         j-=1
            
                
        # return len(arr)-x