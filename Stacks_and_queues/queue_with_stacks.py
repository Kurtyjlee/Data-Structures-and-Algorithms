# Implementing a queue using stacks only. Using stacks only to achieve FIFO.

# Solution: Using an enqueue stack and dequeue stack. The enqueue stack will be
# used for insertion and the dequeue stack will be used for pop() or peek()
# When popping data, data from enqueue stack till be popped into the dequeue stack.
# This maintains the first in first out order.The enqueue stack is basically flipped
# So the FIFO order is maintained

class Queue:
    def __init__(self):
        # For enqueuing
        self.enq_stack = []
        # For dequeuing
        self.deq_stack = []

    # Insert data into the enqueue stack
    def enqueue(self, data):
        self.enq_stack.append(data)

    def dequeue(self):
        if len(self.enq_stack) == 0 and len(self.deq_stack) == 0:
            print("Stacks are empty...")
            return
        
        if len(self.deq_stack) == 0:
            while len(self.enq_stack) != 0:
                self.deq_stack.append(self.enq_stack.pop())
            
        return self.deq_stack.pop()

if __name__=="__main__":
    queue = Queue()

    for i in range(10):
        queue.enqueue(i)

    print(queue.enq_stack)
    for _ in range(10):
        print(queue.dequeue())
