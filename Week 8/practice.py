"""
Problem: complete the append method in the LinkedList class. This method should create a new node with the provided data and add it to the end of the linked list. If the linked list is empty, the new node should become the head of the list.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    # Initialize the linked list
    def __init__(self):
        self.head = None
        
    # This method will add a new node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    # This method will print the linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def search(self, data):
        cur_node = self.head
        found = False
        position = 0  # Add the missing variable position
        while cur_node != None and not found:
            if cur_node.data == data:  # Correct the attribute access to cur_node.data
                found = True
                return f'{data} is in the list at position {position}'
            else:
                cur_node = cur_node.next  # Correct the attribute access to cur_node.next
                position += 1
        return found
    
    def remove(self, data):
        cur_node = self.head
        previous = None
        found = False
        while not found:
            if cur_node.data == data:  # Correct the attribute access to cur_node.data
                found = True
            else:
                previous = cur_node
                cur_node = cur_node.next  # Correct the attribute access to cur_node.next
                
        if previous == None:
            self.head = cur_node.next  # Correct the attribute access to cur_node.next
        else:
            previous.next = cur_node.next  # Correct the attribute access to cur_node.next
                        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_list()
print()
ll.remove(1)
ll.print_list()
print()

print(ll.search(3))
