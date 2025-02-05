'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    curr = head #temp current pointer pointing to head of list
    prev = None #temp previous pointer pointing to nothing for now and will be update in loop
    while curr: #while there is a node in the list available
        temp = curr.next
        curr.next = prev #where the list gets flipped
        prev = curr #moving the previous pointer to where the curr was pointing 
        curr = temp #moving the curr pointer to where temp was pointing
    return prev
        
# This is the iterative approach with time complexity of O(n) and space complexity of O(1)
