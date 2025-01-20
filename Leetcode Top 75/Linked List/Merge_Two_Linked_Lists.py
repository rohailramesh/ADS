# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # First use a dummy node pointing to nowhere for now and a current pointer pointing to that dummy
        # In the while loop as we compare l1 val and l2 val, we can update the current pointer
        # Once loop through both lists is complete and still there are elements left in either list, we can just point the current pointer to that list
        dummyNode = ListNode(0)
        current_pointer = dummyNode
        
        while list1 and list2:
            if list1.val < list2.val:
                current_pointer.next = list1  # Link current pointer to list1
                list1 = list1.next
            else:
                current_pointer.next = list2  # Link current pointer to list2
                list2 = list2.next
            current_pointer = current_pointer.next  # Move the current pointer forward
        
        # If any list is not empty, link it to the end of the merged list
        if list1:
            current_pointer.next = list1
        elif list2:
            current_pointer.next = list2
        
        return dummyNode.next  # Return the merged list starting from the next node of dummyNode
