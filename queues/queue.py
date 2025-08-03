from .node import Node

class Queue():
    def __init__(self):
        self._front = None
    
    def enqueue(self, data):
        if self.is_empty():
            self._front = Node(data)
            return self._front.data
        current_node = self._front
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)
        return current_node.next.data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue: can't dequeue more objects")
        dequeued_node = self._front
        self._front = self._front.next
        return dequeued_node.data

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def __str__(self):
        msg = ""
        for index, value in enumerate(self):
            if index == 0:
                msg += str(value)
            else:
                msg += "->" + str(value)
        return msg

    def __iter__(self):
        current_node = self._front
        while current_node:
            yield current_node.data
            current_node = current_node.next           

    def __add__(self, other):
        new_queue = Queue()
        for i in self:
            new_queue.enqueue(i)
        for i in other:
            new_queue.enqueue(i)
        return new_queue

    def is_empty(self):
        return self._front is None