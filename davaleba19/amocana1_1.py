# create a Node class
class Node:
    def __init__(self, data):
        # initialize object with given data and info about next object
        self.data = data
        self.next = None


# create a LinkedList class
class LinkedList:
    def __init__(self):
        # initialize first - head object
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        current_index = 0
        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next
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