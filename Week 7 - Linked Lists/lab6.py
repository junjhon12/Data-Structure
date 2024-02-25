"""
Linked List is a data structure that consists of a sequence of elements. Each element contains a link to the next element in the sequence. This allows for easy access to the elements of the linked list. This allows for easy access to the elements of the linked list.

CRUD stands for Create, Read, Update, and Delete. This is a set of operations that can be performed on a data structure. This is a set of operations that can be performed on a data structure.

How to create a linked list using python?
    - You can create a linked list using python by using the Node class. The Node class contains a data attribute and a next attribute. The data attribute contains the data of the node. The next attribute contains the link to the next node in the sequence. This allows for easy access to the elements of the linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #reference to the next node
        
class LinkedList:
    def __init__(self):
        self.head = None
    # This method appends a new node with the data to the end of the linked list.
    def append(self, data):
        # This method appends a new node with the data to the end of the linked list.
        new_node = Node(data)
        # If the linked list is empty, then the new node is the head of the linked list.
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        # If the linked list is not empty, then the new node is added to the end of the linked list.
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # This method deletes the node with the data from the linked list.
    def print_list(self):
        cur_node = self.head
        # This method prints the elements of the linked list.
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
ll = LinkedList()


ll.append(1)
ll.append(20)
ll.append(20)
ll.append(4)
ll.print_list()

# How to access the elements of the linked list?
#     - The elements of the linked list are accessed by using the head of the linked list and the next attribute of the node. This allows for easy access to the elements of the linked list.

# How to append an element to the linked list?
#     - You can append an element to the linked list by using the append method. The append method creates a new node with the data and adds it to the end of the linked list. This allows for easy addition of elements to the linked list.

# How to print the elements of the linked list?
#     - You can print the elements of the linked list by using the print_list method. The print_list method prints the elements of the linked list. This allows for easy printing of the elements of the linked list.

# How to delete an element from the linked list?
#     - You can delete an element from the linked list by using the delete method. The delete method removes the node with the data from the linked list. This allows for easy deletion of elements from the linked list.

# How to update an element in the linked list?
#     - You can update an element in the linked list by using the update method. The update method updates the data of the node with the new data. This allows for easy updating of elements in the linked list.

# How to search for an element in the linked list?
#     - You can search for an element in the linked list by using the search method. The search method searches for the node with the data in the linked list. This allows for easy searching of elements in the linked list.

def __init__(self, data):
    self.data = data
    self.ref = None

def __init__(self):
    self.head = None
    
def print_LL(self):
    if self.head is None:
        print("Linked List is empty")
    else:
        n = self.head
        while n is not None:
            print(n.data, "-->", end=" ")
            n = n.ref
            
LL = LinkedList()
LL.append(10)
LL.print_LL() # Linked List is empty

#Advantages of using linked list:
#     - The linked list is a dynamic data structure. This means that the size of the linked list can change during the execution of the program. This allows for easy addition and deletion of elements from the linked list.
#     - The linked list is a flexible data structure. This means that the elements of the linked list can be accessed in any order. This allows for easy access to the elements of the linked list.
#     - The linked list is a memory-efficient data structure. This means that the elements of the linked list are stored in a memory-efficient way. This allows for easy storage of elements in the linked list.