class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:    
        
        
        # fast = head
        # slow = head
        
        # # Move the fast pointer n steps ahead
        # for _ in range(n):
        #     fast = fast.next
        
        # # If fast is None, it means we need to remove the first node
        # if fast is None:
        #     return head.next
        
        # # Move both pointers until fast reaches the end of the list
        # while fast.next is not None:
        #     fast = fast.next
        #     slow = slow.next
        
        # # Now, slow is pointing to the node before the one to be deleted
        # slow.next = slow.next.next
        
        # return head


# Create a dummy node to handle edge cases where the head itself needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers together until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        # Return the new head of the list
        return dummy.next
