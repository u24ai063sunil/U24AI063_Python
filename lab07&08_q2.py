class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.items)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

print("Dequeued:", queue.dequeue()) 
print("Peek:", queue.peek()) 

queue.display() # Output: Queue:

print("Size:", queue.size())

print("Dequeued:", queue.dequeue()) 
print("Dequeued:", queue.dequeue()) 
print("Dequeued:", queue.dequeue()) 
queue.display() 
