class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ha={}
        ha2={}
        if len(s)==len(t):
            for ele in s:
                if ele in ha:
                    ha[ele]+=1
                else:
                    ha[ele]=1
            for ele2 in t:
                if ele2 in ha2:
                    ha2[ele2]+=1
                else:
                    ha2[ele2]=1
            
            # print(ha, ha2)
            if ha==ha2:
                return True
