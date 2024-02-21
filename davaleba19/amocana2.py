# Create a Node class
class Node:
    def __init__(self, data):
        # Initialize object with given data and info about next object
        self.data = data
        self.next = None


class LinkedList:
    # Initialize first - head object
    def __init__(self):
        self.head = None

    # Append a new node with given data to the end of the linked list
    def append(self, data):
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

    def display_info(self):
        # Start from the head of the linked list
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            # Move to the next node
            current_node = current_node.next
        print()


# Create a new linked_list object
linked_list = LinkedList()
# Append elements to the linked list and display info
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.display_info()
