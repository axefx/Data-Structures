"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # handle if a node type is given
        if type(value)!= int and value != None:
            value = value.value
        # if list is empty 
        if self.head == None:
            # create a node from value
            newnode = ListNode(value)
            # assigned to head and tail
            self.head = newnode
            self.tail = self.head
        # handle not empty list
        elif self.length > 0:
            # while head is not the last item
            current = self.head
            while current.next is not None:
                # set tail to the last item
                self.tail= current.next
                # update current to the next node
                current = current.next
            # create a new node before head with value
            self.head.insert_before(value)
            # set head = the new node
            self.head = self.head.prev
        self.length +=1
        return self.head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if type(value)!= int:
            value = value.value
        # if empty list return as head
        if self.head == None:
            newnode = ListNode(value)
            self.head = newnode
            self.tail = self.head
        elif self.length > 0:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length +=1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node)
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if list is empty
        if self.head == None:
            self.head = None
            self.tail = None
        # if list is one
        elif self.length == 1:
            self.head = None
            self.tail = None
        # else if node is head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # else if node is tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # if its in between two nodes
        else:
            curr = self.head
            while curr.next != None:
                if node == curr:
                    curr.prev.next = node.next
                    curr.next.prev = node.prev
                    node.delete()
                curr = curr.next
            self.tail = curr
        self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if head is empty return None
        if self.head == None:
            return None
        # set max value with the head value
        max_val = self.head.value
        # loop through next nodes
        current_node = self.head.next
        while current_node is not None:
            if current_node.value > max_val:
                max_val = current_node.value

            current_node = current_node.next

        return max_val
    

if __name__ == "__main__":
    node = ListNode(1)
    dll = DoublyLinkedList(node)
    print(f"dll: {dll}")
    print(f"length: {dll.length}")
    dll.remove_from_tail()
    print(f"length: {dll.length}")
    dll.add_to_tail(33)
    print(f"length: {dll.length}")
    print(f"head: {dll.head.value}")
    print(f"tail: {dll.tail.value}")
    print(f"removing...: {dll.remove_from_tail()}")
    curr_head = dll.head
    while curr_head is not None:
        print(f"values: {curr_head.value}")
        curr_head = curr_head.next

    # dll.delete(dll.head)

    # curr_head = dll.head
    # while curr_head is not None:
    #     print(f"values: {curr_head.value}")
    #     curr_head = curr_head.next
    print(f"length: {dll.length}")
