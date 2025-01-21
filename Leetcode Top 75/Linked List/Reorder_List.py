'''
Given a singly linked list L: L0 → L1 → ... → Ln-1 → Ln,

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Optimised solution approach with time complexity of O(n) and space complexity of O(1)
# Take the linked list and split it in half using a slow and fast pointer to find the mid
# Once the mid has been found take the second half of the list and reverse it.
# After second list is reversed, use two temp pointers for each list and updat each one by pointing their next to whichever link it should be

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # base check if list is empty
        if not head:
            return
        
        # -------------
        # Finding the mid point of a list using a fast and slow pointer
        # First half l1 is before mid point
        # Second half l2 is after mid point
        
        # start by pointing both pointers to head and fast will move twice as
        # fast as slow so by time fast gets to end of list, slow will be at mid
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        
        #-----------------
        # Process of reversing the list
        prev = None
        cur = mid
        while cur:
            cur.next = prev
            prev = cur
            cur = cur.next
        head_of_second = prev
        
        # -------
        # Merging the two lists together by updating the two links by alternating
        first = head
        second = head_of_second
        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop