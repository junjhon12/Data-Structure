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
        return found            
            
llist = LinkedList()

llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(5)
llist.print()
llist.search(4)