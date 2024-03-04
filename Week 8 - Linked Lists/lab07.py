"""
Create a Linked List data structure by writing your own node class.
Just the way we explored it in the Lecture, your node class will house the data
(integer in this case) and a pointer to the next node element. Populate your
linked list with the following integers and print it .
1,50, 11, 33, 21, 40, 71
No you do not need to print the commas ;)
Delete N-th node from the end of the linked list and print the linked list after deletion. Here N = 2
Below is the expected output after deleting the second last element.
1,50, 11, 33, 21, 71
ATTN : Note : Here we do not know the length of the list.
Complete the above deletion operation without calculating the length of the list.
Your solution should only make a single pass through the linked list, adhering
to O(n) time complexity overall and O(1) space complexity.
"""
# This class will create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    # This method will add a new node to the end of the list
    def add(self, data):
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
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("NULL")
    # This method will remove the n-th node from the end of the list
    def remove(self, n):
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
        
    
        
ll = LinkedList()
ll.add(1)
ll.add(50)
ll.add(11)
ll.add(33)
ll.add(21)
ll.add(40)
ll.add(71)
ll.print_list()
ll.remove(2)
ll.print_list()

# Test cases for LinkedList

# Null test case
ll_null = LinkedList()
ll_null.remove(2)  # Trying to remove from an empty list
ll_null.print_list()

# One element test case
ll_one = LinkedList()
ll_one.add(1)
ll_one.remove(2)
ll_one.print_list()

# Two elements test case
ll_two = LinkedList()
ll_two.add(1)
ll_two.add(2)
ll_two.remove(2)
ll_two.print_list()

# Three elements test case
ll_three = LinkedList()
ll_three.add(1)
ll_three.add(2)
ll_three.add(3)
ll_three.remove(2)
ll_three.print_list()

# Same element test case
ll_same = LinkedList()
ll_same.add(1)
ll_same.add(1)
ll_same.add(1)
ll_same.remove(2)
ll_same.print_list()
