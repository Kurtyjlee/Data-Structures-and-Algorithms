# Implementing queues in python; First in first out structure

class Queue:
    def __init__(self):
        # Using an array for this queue. A linked list can be used as well.
        self.queue = []

    def is_empty(self):
        return self.queue == []

    # O(1) running time as the item is inserted to the back
    def enqueue(self, data):
        self.queue.append(data)
    
    # Returning the first item of the queue and removing it O(n)
    # Removing the first item from an array is O(n)
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[0]
        del self.queue[0] 
        return data

    # Return the last item of the queue O(1)
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def size_queue(self):
        return len(self.queue)

if __name__=="__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    print(f"Size: {queue.size_queue()}")
    print(f"Last item: {queue.peek()}")