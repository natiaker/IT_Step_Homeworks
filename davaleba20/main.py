# Create a node class
class Node:
    # Initialize object with given value, and left child and right child
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to print leaf nodes
def printLeafNodes(node):
    # If node is none, return
    if node is None:
        return
    # If node has no child - left and right - nodes, it is a leaf node
    if node.left is None and node.right is None:
        print(f"Leaf node: {node.value}")
    # Call recursion for left and right child nodes
    printLeafNodes(node.left)
    printLeafNodes(node.right)


# function to count edges
def countEdges(node):
    # If node doesn't exist, return 0 edges
    if node is None:
        return 0
    # If node has no children, return 0
    if node.left is None and node.right is None:
        return 0
    # If node has no left child, it has right child and adds 1, same for the right child
    if node.left is None:
        return 1 + countEdges(node.right)
    if node.right is None:
        return 1 + countEdges(node.left)
    # if node has 2 children, add 2
    return 2 + countEdges(node.left) + countEdges(node.right)


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
printLeafNodes(root)
print(countEdges(root))
