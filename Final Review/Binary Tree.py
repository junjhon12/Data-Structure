
class Tree_Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
     
def print_tree(root):
    result = []
    q = []  # Use a regular list instead of collections.deque()
    q.append(root)
    while q:
        var = q.pop(0)  # Use pop(0) to remove the first element
        result.append(var.value)
        if var.left:
            q.append(var.left)
        if var.right:
            q.append(var.right)
    print(result)
        
def inorder_iterative(root):
    result = []
    deque = []  # Use a regular list instead of collections.deque()
    current = root
    while current or len(deque) > 0:
        if current:
            deque.append(current)
            current = current.left
        else:
            current = deque.pop()
            result.append(current.value)
            current = current.right
    return result

def insert(root, value):
    if root is None:
        return Tree_Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def level_order_traversal(root):
    result = []
    q = []  # Use a regular list instead of collections.deque()
    q.append(root)
    while q:
        current = q.pop(0)  # Use pop(0) to remove the first element
        result.append(current.value)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return result

def find_min(root):
    current = root
    # Traverse to the leftmost node since it will be the smallest
    while current.left:
        current = current.left
    return current

def validBST(node, lower_bound, upper_bound):
    # A Null node is a valid BST
    if node is None:
        return True
    if node.value > lower_bound and node.value < upper_bound:
        return False
    if node.value <= lower_bound or node.value >= upper_bound:
        return False
    return validBST(node.left, lower_bound, node.value) and validBST(node.right, node.value, upper_bound)

def find_kth_smallest(root, k):
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.value
            current = current.right
    return None
            
root = Tree_Node(4)
root.left = Tree_Node(2)
root.right = Tree_Node(6)
root.left.left = Tree_Node(1)
root.left.right = Tree_Node(3)
root.right.left = Tree_Node(5)
root.right.right = Tree_Node(7)
print_tree(root)
print(inorder_iterative(root))
print(level_order_traversal(root))
print(find_min(root).value)
print(level_order_traversal(root))
print(validBST(root, float('-inf'), float('inf')))
print(find_kth_smallest(root, 3))

