"""
Create a Linked List data structure by writing your own node class.
Just the way we explored it in the Lecture, your node class will house the data
(integer in this case) and a pointer to the next node element. Populate your
linked list with the following integers and print it .
1
50, 11, 33, 21, 40, 71
No you do not need to print the commas ;)
Delete N-th node from the end of the linked list and print the linked list after deletion. Here N = 2
Below is the expected output after deleting the second last element.
50, 11, 33, 21, 71
ATTN : Note : Here we do not know the length of the list.
Complete the above deletion operation without calculating the length of the list.
Your solution should only make a single pass through the linked list, adhering
to O(n) time complexity overall and O(1) space complexity.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
        
    def delete_nth_node(self, n):
        fast = self.head
        slow = self.head
        for i in range(n):
            fast = fast.next
        if not fast:
            self.head = self.head.next
            return
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        
        
ll = LinkedList()
ll.insert(50)
ll.insert(11)
ll.insert(33)
ll.insert(21)
ll.insert(40)
ll.insert(71)
print(ll.print_list())
ll.delete_nth_node(2)
print(ll.print_list())