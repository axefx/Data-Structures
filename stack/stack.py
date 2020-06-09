"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise RuntimeError("empty stack")
        last_in = self.size - 1
        last_item = self.storage[last_in]
        del self.storage[last_in]
        self.size-=1
        return last_item

if __name__ == "__main__":
    print("class Stack: version 1")
    # create stack
    astack = Stack()

    # push 0-9 into stack with 9 on top
    for i in range(10):
        astack.push(i)

    # print length of stack
    print(f"length: {len(astack)}")

    # show current storage
    print(f"storage: {astack.storage}")

    # pop the 9 out
    print(f"last in/first out: {astack.pop()}")

    # show current storage
    print(f"storage: {astack.storage}")

    # length should be 1 less
    print(f"length: {len(astack)}")

    print("----------"*8)

from ..singly_linked_list.singly_linked_list import LinkedList

class Stack2:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise RuntimeError("empty stack")
        # last_in = self.size - 1
        # last_item = self.storage[last_in]
        # del self.storage[last_in]
        self.size-=1
        # return last_item
        return self.storage.remove_tail()


if __name__ == "__main__":
    print("class Stack: version 2")
    # create stack
    astack = Stack2()

    # push 0-9 into stack with 9 on top
    for i in range(10):
        astack.push(i)

    # print length of stack
    print(f"length: {len(astack)}")

    # show current storage
    print(f"storage tail: {astack.storage.tail.value}")

    # pop the 9 out
    print(f"last in/first out: {astack.pop()}")

    # show current storage
    print(f"storage tail: {astack.storage.tail.value}")

    # length should be 1 less
    print(f"length: {len(astack)}")