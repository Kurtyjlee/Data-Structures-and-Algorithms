# Implementing queues using stacks with recursion.

# Solution: Only 1 stack needs to be define, with recursion, but 2 stacks worth of 
# memory is still used. 1 stack is called and the other stack used is the system
# stack.

class Queue:
    def __init__(self):
        self.stack = []

    # Insert data into the enqueue stack
    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):
        # Base case
        if len(self.stack) == 1:
            return self.stack.pop()

        # Saving the item as a variable first
        item = self.stack.pop()

        # Calling the method recursively until the first item is found
        dequeued_item = self.dequeue()

        # Will execute sequentially as the functions are removed from the system stack
        self.stack.append(item)

        return dequeued_item

if __name__=="__main__":
    queue = Queue()

    for i in range(10):
        queue.enqueue(i)
    print(queue.stack)
    for _ in range(10):
        print(queue.dequeue())