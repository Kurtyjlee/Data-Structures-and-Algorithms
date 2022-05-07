# Construct an algorithm, without extra memory, to find the middle node of the
# linked list O(n)

# Solution 1: iterate through the whole list and find the number of elements. The
# node with index len(linked_list) / 2 is the middle node.
# 
# Solution 2: Using 2 pointers, get the middle node. First pointer will traverse
# the linked list 1 node at a time, while the second pointer, 2 nodes at a time.
# When second pointer is at the end, the first pointer will be at the middle.

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

# Making of the linked list data structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # Algorithm to get the middle node
    def get_middle(self):
        fast_pointer = self.head
        slow_pointer = self.head

        # Cehck that it is not at the end of the linked list
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        # Slow pointer is now the middle node
        return slow_pointer

    def insert_start(self, data):
        # Creating a node object
        new_node = Node(data)
        self.num_of_nodes += 1

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1

        if self.head is None:
            self.head = new_node
        else:
            pointer_node = self.head
            while pointer_node.next_node is not None:
                pointer_node = pointer_node.next_node
            pointer_node.next_node = new_node

    # Test if the linked list is working fine O(n)
    def traverse(self):
        pointer_node = self.head

        while pointer_node is not None:
            print(pointer_node)
            pointer_node = pointer_node.next_node

    # O(1) for first item and O(n) for other items
    def remove(self, data):
        if self.head is None:
            return

        pointer_node = self.head
        previous_node = None

        while pointer_node is not None and pointer_node.data != data:
            previous_node = self.head
            pointer_node = pointer_node.next_node

        if pointer_node is None:
            print("Data not found")
            return
        
        # Removal of node
        if previous_node is None:
            self.head = pointer_node.next_node
        else:
            previous_node.next_node = pointer_node.next_node

if __name__=="__main__":
    linked_list = LinkedList()
    for i in range(11):
        linked_list.insert_start(i)
    linked_list.traverse()
    print(linked_list.get_middle())