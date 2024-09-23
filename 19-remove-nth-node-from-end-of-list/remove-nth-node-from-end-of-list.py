class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is None, it means we need to remove the first node
        if fast is None:
            return head.next
        
        # Move both pointers until fast reaches the end of the list
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        # Now, slow is pointing to the node before the one to be deleted
        slow.next = slow.next.next
        
        return head




        
        
        
        # # Create a dummy node to handle edge cases where the head itself needs to be removed.
        # dummy = ListNode(0)
        # dummy.next = head
        # first = dummy
        # second = dummy

        # # Advance the first pointer by n + 1 nodes.
        # for _ in range(n + 1):
        #     first = first.next

        # # Move both pointers together until the first pointer reaches the end.
        # while first is not None:
        #     first = first.next
        #     second = second.next

        # # Remove the nth node from the end.
        # second.next = second.next.next

        # return dummy.next
