class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for char in s:
            if st and st[-1] != char and st[-1].lower() == char.lower():
                st.pop()  
            else:
                st.append(char)

        # i=0
        # while i<len(s):
        #     st.append(s[i])
        #     if s[i].lower()==st[-1] or s[i].upper()==st[-1]:
        #         st.remove(st[-1])
        #         i+=1
        #     i+=1

        return ''.join(st)
