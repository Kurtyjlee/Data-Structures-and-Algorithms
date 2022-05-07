# Construct an algorithm to reverse a linked list

# Solution: Using 4 pointers; prev, next, head and current. Using the current node,
# next node and previous node, the linked list can have their pointers flipped,
# reversing the linked list.

# The current node will point to the previous node. Then the previous node will
# pointer to the current node and the current node will point to the next node.
# The next node points to the next and the algorithm continues. The head will point
# at the last node, completing the flip.

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

    # Reversing the linked list
    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        # While not beyond the linked list
        while current_node:
            next_node = current_node.next_node
            # Current node pointing to the previous node
            current_node.next_node = previous_node
            # Previous node pointing to the current node, moving along the list
            previous_node = current_node
            # Current node pointer also moves along the linked list
            current_node = next_node
        # At the end, the previous node will be pointing to the last elemenet of
        # the linked list, hence it becomes the new head
        self.head = previous_node

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
    print("reversed")
    linked_list.reverse()
    linked_list.traverse()