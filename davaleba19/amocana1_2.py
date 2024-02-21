# Node class to create nodes for the stack
class Node:
    # Initialize a node with given data
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Initialize an empty stack
    def __init__(self):
        self.top_node = None
        self.length = 0    # Length of the stack

    # Check if the stack is empty
    def empty(self):
        return self.length == 0

    # Return the size of the stack
    def size(self):
        return self.length

    def top(self):
        # If stack is not empty return top node data, if empty - raise IndexError
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")

    # Add a new node with given data to the top of the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node

        # new node is being set to refer to the current top node
        new_node.next = self.top_node
        # Update the top node to be the new node
        self.top_node = new_node
        # Increase the size of the stack
        self.length += 1

    # If stack is not empty, remove and return the data of the top node from the stack, if it's empty raise IndexError
    def pop(self):
        if not self.empty():
            # Get the data of the top nodde
            popped_item = self.top_node.data
            # Update the top node to the previous node
            self.top_node = self.top_node.next
            # Decrease the length of the stack
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack Is Empty")


# Create a new stack object
stack = Stack()
print(stack.size())
# Add/push a new element to the top of the stack
stack.push(1)
stack.push(5)
stack.push(10)
# Print the stack's size
print(stack.size())
# remove/pop the top element
print(stack.pop())
# print top element
print(stack.top())
