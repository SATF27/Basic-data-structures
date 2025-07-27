from abc import ABC, abstractmethod
from stacks.stack import Stack

class BinaryTree(ABC):
    class _Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self._root = None

    @abstractmethod
    def insert(self, data):
        pass
    
    @abstractmethod
    def find(self, data):
        pass

    def __str__(self):
        msg = "root: " + str(self._root.data) + "\n"
        msg += "nodes: ["
        for index, value in enumerate(self):
            if index == len(self) - 1:
                msg += str(value) + "]"
            else: 
                msg += str(value) + ", "
        return msg
            
    def __len__(self):
        length = 0
        for _ in iter(self):
            length += 1
        return length
    
    # iterates over the tree using preorder traversal
    def __iter__(self):
        if self._root is not None:
            stack_roots = Stack()
            stack_roots.push(self._root)
        while not stack_roots.is_empty():
            current_node = stack_roots.pop()
            yield current_node.data
            if current_node.right is not None:
                stack_roots.push(current_node.right)
                print(current_node.right.data, "is at right and its father is", current_node.data)
            if current_node.left is not None:
                print(current_node.left.data, "is at left and its father is", current_node.data)
                stack_roots.push(current_node.left)

    def is_empty(self):
        return self._root is None
            