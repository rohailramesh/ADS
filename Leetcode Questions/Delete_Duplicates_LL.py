# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head):
        dummy = ListNode() #create a dummy node before first node
        dummy.next = head #point the pointer to where the head is pointing
        curr = dummy #current is dummy

        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                temp = curr.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                curr.next = temp.next
            else:
                curr = curr.next
        return dummy.next