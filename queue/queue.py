"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size+=1

    def dequeue(self):
        if self.size == 0:
            raise RuntimeError("empty queue")
        self.size-=1
        return self.storage.pop(0)

if __name__ == "__main__":
    print("Queue with list as storage")
    a_queue = Queue()
    print(f"a_queue: {a_queue}")
    for i in range(10):
        a_queue.enqueue(i)
    print(f"a_queue len: {len(a_queue)}")
    print(f"a_queue storage: {(a_queue.storage)}")
    print("dequeue a value...")
    print(f"a_queue dequeue: {(a_queue.dequeue())}")
    print(f"a_queue storage: {(a_queue.storage)}")
    print(f"a_queue len: {len(a_queue)}")
    

    print("----------"*8)

from ..singly_linked_list.singly_linked_list import LinkedList

class Queue2:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size+=1

    def dequeue(self):
        if self.size == 0:
            raise RuntimeError("empty queue")
        self.size-=1
        return self.storage.remove_head()

if __name__ == "__main__":
    print("Queue with linked list as structure")
    a_queue = Queue2()
    print(f"a_queue: {a_queue}")
    for i in range(10):
        a_queue.enqueue(i)
    print(f"a_queue len: {len(a_queue)}")
    print(f"a_queue head: {(a_queue.storage.head.value)}")
    print("dequeue a value...")
    print(f"a_queue dequeue: {(a_queue.dequeue())}")
    print(f"a_queue head: {(a_queue.storage.head.value)}")
    print(f"a_queue len: {len(a_queue)}")
    

    print("----------"*8)

## stretch
from ..stack.stack import Stack

class Queue3:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.push(value)
        self.size+=1

    def dequeue(self):
        if self.size == 0:
            raise RuntimeError("empty queue")
        self.size-=1
        return self.storage.pop()

if __name__ == "__main__":
    print("Queue with stacks")
    a_queue = Queue3()
    print(f"a_queue: {a_queue}")
    for i in range(10):
        a_queue.enqueue(i)
    print(f"a_queue len: {len(a_queue)}")
    print(f"a_queue head: {(a_queue.storage.storage)}")
    print("dequeue a value...")
    tempStack = Stack()
    for i in range(len(a_queue)-1):
        tmp = a_queue.dequeue()
        tempStack.push(tmp)
        a_queue.enqueue(tempStack.pop())
    # print(f"a_queue dequeue: {(a_queue.dequeue())}")
    print(f"a_queue head: {(a_queue.storage.storage)}")
    print(f"a_queue len: {len(a_queue)}")
