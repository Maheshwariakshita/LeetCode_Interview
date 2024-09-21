# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #rec
        if head is None or head.next is None:
            return head
        curr=head
        prev=None
        a=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        # while curr:
        #     curr_temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=curr_temp
        head.next=None
        return a


# ll rev-iter
        # if head is None:
        #     return head
        # curr=head
        # prev=None
        # while curr:
        #     curr_temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=curr_temp
        # head.next=None
        # return prev

        
        








        # prev = None
        # curr = head
        # while curr:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
            
        # return prev