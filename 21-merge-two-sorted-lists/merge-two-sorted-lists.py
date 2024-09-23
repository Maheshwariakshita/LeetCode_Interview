# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        

        dummy=ListNode(0)
        curr=dummy
        h1=list1
        h2=list2
        while h1!=None and h2!=None:
            if h1.val <=h2.val:
                curr.next=h1
                h1=h1.next
            else:
                curr.next=h2
                h2=h2.next
            curr=curr.next
        while h1!=None:
            curr.next=h1
            h1=h1.next
            curr=curr.next
        while h2!=None:
            curr.next=h2
            h2=h2.next
            curr=curr.next
        return dummy.next








        # dummy=curr=ListNode(0)
      
        # if list1==None:
        #     return list1
        # if list2==None:
        #     return list2
        
        # while list1!=None and list2!=None:
        #     if list1.val<=list2.val:
        #         dummy.next=list1
        #         list1=list1.next
        #     else:
        #         dummy.next=list2
        #         list2=list2.next
        #     dummy=dummy.next
        # if list1!=None:
        #     dummy.next=list1
        # else:
        #     dummy.next=list2
        # return curr.next