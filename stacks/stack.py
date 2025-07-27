from .node import Node

class Stack():
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if (self.top is None):
            self.top = new_node 
            return self.top.data
        previous = self.top
        self.top = new_node
        self.top.previous = previous

    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack: can't pop more objects")
        top_node = self.top
        self.top = self.top.previous
        return top_node.data       

    def __str__(self):
        msg = ""
        for index, value in enumerate(self):
            if index == 0:
                msg += str(value)
            else:
                msg += "->" + str(value)
        return msg

    def __len__(self):
        length = 0
        for i in iter(self):
            length += 1
        return length
    
    def is_empty(self):
        return self.top is None
    
    def __iter__(self):
        current_node = self.top
        while current_node:
            yield current_node.data
            current_node = current_node.previous