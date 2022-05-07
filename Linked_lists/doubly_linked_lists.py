# Implementation for a doubly linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Doubly linked list usually inserts items to the end of the linked list.
    def insert_end(self, data):
        new_node = Node(data)

        # For the first node, both head node and tail node are the same
        if self.head:
            self.head = new_node
            self.tail = new_node
        # Insert the new node to the end of the linked list
        else:
            # The old tail becomes the previous node of the newly inserted node
            new_node.previous = self.tail
            # tail is always pointing to the last node
            self.tail.next = new_node
            # new node becomes new tail
            self.tail = new_node

    def traverse_forward(self):
        pointer_node = self.head

        # Last node will always point to None, hence when beyond last node,
        # pointer_node is None
        while pointer_node:
            print(pointer_node.data)
            pointer_node = pointer_node.next

    def traverse_backward(self):
        pointer_node = self.tail

        # Beyond the first node will be None as well
        while pointer_node:
            print(pointer_node.data)
            pointer_node = pointer_node.previous

if __name__=="__main__":
    linkedlist = DoublyLinkedList()
    for i in range(10):
        linkedlist.insert_end(i)
    linkedlist.traverse_forward()
    linkedlist.traverse_backward()