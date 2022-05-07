# Implement an algorithm that can return the maximum item of a stack in O(1)

# Solution: Fill up the main stack and a max stack simultaneously, only storing the
# max number in the max stack. When grabbing the max item, peek() can be used. When
# pop() is used on the main stack, pop() and can called on the max stack as well.

class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        # If the item on the main stack is its only item
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return
        # Checking if the data is more than the current max value
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        # Duplicate the last value if data is less than the current max value
        else:
            self.max_stack.append(self.max_stack[-1])
    
    def pop(self):
        if self.is_empty():
            return None
        data = self.main_stack[-1]
        # Remove both items from both stacks
        del self.main_stack[-1]
        del self.max_stack[-1]

        return data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.main_stack[-1]

    def is_empty(self):
        return self.main_stack == []

    def stack_size(self):
        return len(self.main_stack)

    # Returning the last value of the max stack
    def get_max(self):
        return self.max_stack[-1]

if __name__=="__main__":
    stack = MaxStack()
    for i in range(10):
        stack.push(i)
    print(f"Size: {stack.stack_size()}")
    print(f"Last item: {stack.peek()}")
    print(f"Max item: {stack.get_max()}")