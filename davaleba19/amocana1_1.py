# Create a Node class
class Node:
    def __init__(self, data):
        # Initialize object with given data and info about next object
        self.data = data
        self.next = None


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        # Initialize first - head object
        self.head = None

    # Create append method
    def append(self, data):
        # Append a new node with given data to the end of the linked list
        new_node = Node(data)

        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Start from the beginning of the linked list
        last_node = self.head

        # While last node's next element exists(is not None) it gets meaning of next element
        while last_node.next:
            last_node = last_node.next

        # When last node's next is None we add new node
        last_node.next = new_node

    # Create insert method
    def insert(self, data, index):
        # Insert a new node with given data at the specified index in the linked list
        new_node = Node(data)

        # If index is 0, insert at the beginning of the linked list
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0
        # Traverse the linked list until reaching the node just before the insertion index
        # (while current node's next is not none and current index < index - 1),
        # move to the next node and increment the index by 1 at each iteration
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        # Connect the new node to the rest of the linked list
        new_node.next = current_node.next
        # Inserting the new node after the current node in the linked list
        current_node.next = new_node

    # Remove the node at the specified index from the linked list
    def remove(self, index):
        # if index is 0, head will be updated to the next element
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_index = 0
        # Traverse to the node just before the target index to locate a specific node in the linked list
        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next
        # Set the next refer of the current node to refer to the node that comes after the next, next node.
        if current_node.next:
            current_node.next = current_node.next.next

    def display_info(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.display_info()
linked_list.insert(11, 1)
linked_list.insert(15, 2)
linked_list.display_info()
linked_list.remove(2)
linked_list.display_info()