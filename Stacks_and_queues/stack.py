# Implementing a stack LIFO structure
# Main functions: push(), pop(), peek()

class Stack:
    def __init__(self):
        # using an array to implement a stack
        self.stack = []

    # Insert item into the stack O(1)
    def push(self, data):
        self.stack.append(data)
    
    # Remove and return the last item we inserted O(1)
    def pop(self):
        if self.is_empty():
            return None
        data = self.stack[-1]
        # Removing the item from the array
        del self.stack[-1]

        return data
    
    # Returns last item without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

if __name__=="__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(f"Size: {stack.stack_size()}")
    print(f"Last item: {stack.peek()}")
