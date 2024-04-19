# Create a linked list
class Node:
    # This is important to initialize the linked list
    def __init__(self, data):
        self.index = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    # This function is to append a new node to the linked list
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def subtract(self, n):
        slow = fast = self.head
        for _ in range(n):
            if fast is None:
                return
            fast = fast.next
        if fast is None:
            self.head = slow.next
            return
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.index)
            temp = temp.next
    # This function is to search for a node in the linked list
    def search(self, data):
        cur_node = self.head
        found = False
        position = 0  # Add the missing variable position
        while cur_node != None and not found:
            if cur_node.index == data:  # Correct the attribute access to cur_node.index
                found = True
                return f'{data} is in the list at position {position}'
            else:
                cur_node = cur_node.next  # Correct the attribute access to cur_node.next
                position += 1
        return 'Data not found in the list'        
    # This function is to remove the n-th node from the end of the linked list
    def remove_node_from_end(self, n):
        # If the linked list is empty, return
        if self.head is None:
            return
        # Use slow and fast since we are traversing the linked list.
        slow = fast = self.head
        # Loop through the linked list, fast will be n nodes ahead of slow.
        for _ in range(n):
            # If fast is None, then n is greater than the length of the list, so return
            if fast is None:
                return
            fast = fast.next
        # If fast is None, then the n-th node from the end is the head, so remove the head.
        if fast is None:
            self.head = slow.next
            return
        # Loop through the linked list, fast will be n nodes ahead of slow.
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Remove the n-th node from the end of the list.
        slow.next = slow.next.next
    # This function is to reverse the linked list
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
    # This function is to check if there is a cycle in the linked list
    def check_cycle(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            # Slow pointer moves one step
            slow = slow.next
            # Fast pointer moves two steps
            fast = fast.next.next
            # If the two pointers meet, then there is a cycle
            if slow == fast:
                return 'True, there is a cycle'
        return 'False, there is no cycle'
    
llist = LinkedList()

llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(5)
llist.print()
print()
llist.remove_node_from_end(2)
llist.print()
print()
llist.reverse_list()
llist.print()
print()
print(llist.check_cycle())
print()
print(llist.search(3))

