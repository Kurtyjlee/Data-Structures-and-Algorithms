# Creating a linked list on python

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    # Representing itself with its data. Must be transformed into a data type
    def __repr__(self):
        return str(self.data)

# Making of the linked list data structure
class LinkedList:
    def __init__(self):
        # First node of the linked list. Access this node exclusively.
        self.head = None
        # Allows the length of the linked list to be retrieve with O(1)
        self.num_of_nodes = 0

    # O(1) insertion running time
    def insert_start(self, data):
        # Creating a node object
        new_node = Node(data)
        self.num_of_nodes += 1

        # New node is the head if there is no head yet
        if self.head is None:
            self.head = new_node
        # Inserting to the front of the linked list
        else:
            # New node points to the head node and then takes over as the head node
            new_node.next_node = self.head
            self.head = new_node
    
    # O(n) insertion running time
    def insert_end(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1

        # Check if the linked list is empty
        if self.head is None:
            self.head = new_node
        # Finding the last node
        else:
            # Starts from the head
            pointer_node = self.head
            # Moves along the linked list to find the end
            while pointer_node.next_node is not None:
                pointer_node = pointer_node.next_node
            # Pointing the last node to the new node, adding it to the end
            pointer_node.next_node = new_node

    # Test if the linked list is working fine O(n)
    def traverse(self):
        pointer_node = self.head

        # At the end of the linked list, last node pointer will point to None
        while pointer_node is not None:
            print(pointer_node)
            pointer_node = pointer_node.next_node

    # O(1) for first item and O(n) for other items
    def remove(self, data):
        if self.head is None:
            return

        pointer_node = self.head
        # Tracking the previous node to allow the "hole" to be patched after removal
        previous_node = None

        # Searching through the linked list to find the node target
        while pointer_node is not None and pointer_node.data != data:
            previous_node = self.head
            pointer_node = pointer_node.next_node

        # Data not found
        if pointer_node is None:
            print("Data not found")
            return
        
        # Removal of node
        # If the target node is the head, new head is the next node
        if previous_node is None:
            self.head = pointer_node.next_node
        else:
            # Linking the previous node to the next node, closing the "hole"
            previous_node.next_node = pointer_node.next_node

if __name__=="__main__":
    linked_list = LinkedList()
    for i in range(1, 11):
        linked_list.insert_end(i)
    linked_list.traverse()
    linked_list.remove(1000)
    # Removing the head node
    linked_list.remove(1)
    # Removing a random node
    linked_list.remove(4)
    linked_list.traverse()