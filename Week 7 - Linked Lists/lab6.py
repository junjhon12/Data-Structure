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

#2/25/2024 Studying Linked Lists
"""
1) There's no requirement that we maintain that positioning in contiguous memory
2) Important note: location of the first item of the list must be explicitly specified. By doing so we can identified where the second is, and so on.
3) Node is the basic building block for linked list implementation. They must hold at least two type of information: data field and reference to the next node.
4) You need to supply the initial data value for the node.
Example:
    class Node:
        def __init__(self, initData):                   temp = Node(93)
            self.data = initData                        temp.getData()
            self.next = None                            Output : 93
            
        def getData(self):
            return self.data
            
        def getNext(self):
            return self.next
            
        def setData(self, newData):
            self.data = newData
        
5) The special Python reference value None will play an important role in the next Node class and later in the linked list itself.
6) A reference to None will denote the fact there is no next node.
7) It's always a good idea to explicitly assign None to your initial next reference values.
8) Unordered list will be built from a collection of nodes, each linked to the next by explicit references.
9) UnorderedList class must maintain a reference to the first node.
Example:
    class UnorderedList:
        def __init__(self):             myList = UnorderedList()
            self.head = None
        
10) It's very important to note that the list class itself does not contain any node objects. Instead it contains sa single reference to only the first node in the linked structure.
Illustration:   myList -> head -> ...
                myList -> head -> 54|_ -> 26|_ -> 93|_ -> 17|_ -> 77|_ -> 31|_ -> ...

11) The isEmpty method checks to see if the head of the list is a refernce to None. self.head==None 
Example:
    def isEmpty(self):
        return self.head == None
        
12) Use the add method to get items into a list but before doing so place the new item in the easiest location possible for unorderedList is the right end.
Example:
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    ...
    
13) Since 31 was added first it'll be the last node on the linked list. First in is last out.
14) The added item shown must reside within an node object.
15) Linking the new node into the existing structure requires two steps:
        1.Change the next reference of the new node
        2.Refer the new node to the old FIRST node
        It's VERY important you follow these steps or else all of the original nodes are and can no longer be accessed.
16) size, search, and remove, are all based on a technique known as linked list traversal.
17) Traversal is the process of systematically visiting each node. Use an external reference that starts at the first node in the list. By moving between nodes, we move the reference to the next node by "traversing" the next reference.
18) size method could be done by traversing the linked list and keep count of the number of nodes that occured.
19) current is the external reference and it's initialized to the head of the list.
Example:
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

20) Boolean variable, found, is use to remmeber wheher we have located the item we are searching for.
Example:
    def search(self, item):                             myList.search(17)
        current = self.head                             Output: True
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        return found
        
21) remove method requires two logical steps:
        1.Traverse the list looking for the item to remove
        2.Once found, remove it.
22) Unfortunatley, there's no way to go backward in the linked list since current refers to the node ahead of the node where we would like to make the change, it is too latee to make the necessary adjustment.
23) The solution: use two external references to traverse down the linked list.
24) In doing so, current stops at the node to be removed, previous will be referrng to proper place in the linked list for the modification.
25) When searching and ite is not found, previous and current must both be moved one node ahead of current. This is because previous is always behind current by one node.
Example:
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
26) insert, index, and pop require that we name the positions of the list.

Part I: Implement the append method for UnorderedList. What is the time complexity of the method you created?
class Node:                                 Time Complexity: O(n)
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()

Part II: In the previous problem, you most likely created an append method that was O(n). If you add an instance variable to the UnorderedList class you can create an append method that is O(1). Modify your append method to be O(1)). Be Careful! To really do this correctly you will need to consider a couple of special cases that may require you to make a modification to the add method as well.
class Node:                                 Time Complexity: O(1)
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()


"""