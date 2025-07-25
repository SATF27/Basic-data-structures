from .list_interface import LinkedList
from .node import Node

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def check_index(self, index):
        if index > len(self) - 1 or index < 0:
            length = len(self)
            raise IndexError(f"index {index} for length {length}")

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            return self._head
        current_node = self._head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return current_node.next
        
    def insert(self, index, data):  
        new_node = Node(data)
        if self.is_empty():
            raise Exception("empty list, items can't be inserted by index")
        self.check_index(index)
        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                new_node.next = current_node.next
                current_node.next = new_node
                return new_node
            current_node = current_node.next
            counter += 1
    
    def remove(self, index):
        if self.is_empty():
            raise Exception("empty list, can't delete more items")
        self.check_index(index)
        previous_node = None
        if index == 0:
            previous_node = self._head
            self._head = self._head.next
            return previous_node
        current_node = self._head
        counter = 0
        while current_node:
            if counter == index:
                previous_node.next = current_node.next
                return current_node
            previous_node = current_node
            current_node = current_node.next
            counter += 1
        raise Exception("while loop failed") # this should not raise never
                
    def __getitem__(self, index):
        self.check_index(index)
        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                return current_node.data
            current_node = current_node.next
            counter += 1

    def __setitem__(self, index, item):
        self.check_index(index)
        counter = 0
        current_node = self._head
        while current_node:
            if counter == index:
                current_node.data = item
                return None
            current_node = current_node.next
            counter += 1

    def __str__(self):
        string_representation = "["
        for i, data in enumerate(self):
            if i == len(self) - 1:
                string_representation += str(data) + "]"
            else:
                string_representation += str(data) + ", "
        return string_representation
    
    def __add__(self, other):
        if self.is_empty():
            raise Exception("can't concatenate an empty list")
        current_node = self._head
        new_list = SinglyLinkedList()
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        current_node = other._head
        while current_node:
            new_list.append(current_node.data)
            current_node = current_node.next
        return new_list
    
    def __len__(self):
        length = 0
        current_node = self._head
        while current_node:
            length += 1
            current_node = current_node.next
        return length