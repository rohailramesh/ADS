class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    # adds new node which points to nothing by default
    # set the next pointer of the new node to previous head pointer
    # point the head to that new node
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printLinkedList(self):
        temp_head = self.head
        while temp_head:
            print(temp_head.data, end=" ")
            temp_head = temp_head.next
        print()
    
    # inserting at end of linked list
    # if linked list is empty then make the item to add as the head
    # if linked list exists then traverse through list till the end and add item and pointer the pointer of previous item to that pointer
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def deleteFromEnd(self):
        # case one - empty linked list
        if self.head is None:
            return
        # case two - only one node in linked list
        if self.head.next is None:
            self.head = None
            return
        # case three - multiple nodes in linked list - go to second last node and point the pointer to none instead
        temp_head = self.head
        while temp_head.next.next:
            temp_head = temp_head.next
        temp_head.next = None
    
    def search(self, value):
        current_head = self.head
        current_position = 0
        while current_head:
            if current_head.data ==  value:
                return current_position
            current_head = current_head.next
            current_position += 1
        return
    
    def deleteDuplicates(self):
        current_head = self.head
        while current_head:
            while current_head.next and current_head.next.data == current_head.data:
                current_head.next = current_head.next.next
            current_head = current_head.next
        return self.head

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insertAtBeginning(1) 
    linked_list.insertAtBeginning(2) 
    linked_list.insertAtBeginning(3) 
    linked_list.insertAtBeginning(3) 
    linked_list.printLinkedList
    linked_list.deleteDuplicates()
    linked_list.printLinkedList()
    