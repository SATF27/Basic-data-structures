from abc import ABC, abstractmethod

class LinkedList(ABC):
    def __init__(self):
        self._head = None

    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def insert(self, index, data):
        pass

    @abstractmethod
    def remove(self, index):
        pass
    
    # getitem and setitem must be implemented to mimic the standard list of python
    @abstractmethod
    def __getitem__(self, index):
        pass
    @abstractmethod
    def __setitem__(self, index, item):
        pass

    # this is supossed to show the list as a string
    @abstractmethod
    def __str__(self):
        pass

    # this is supossed to link this list to another
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def is_empty(self):
        return self._head is None
    
    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.data
            current_node = current_node.next

