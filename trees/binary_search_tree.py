from .binary_tree_interface import BinaryTree
from stacks.stack import Stack

class BinarySearchTree(BinaryTree):
    def insert(self, data):
        if self._root is None: 
            self._root = self._Node(data)
        else: 
            try:
                self._insert(data, self._root)
            except ValueError as e:
                print(e)
            finally:
                return data
        
    # takes the root passed as an argument to compare it to the data that will be inserted
    def _insert(self, data, root):
        if data < root.data:
            if root.left is not None:
                self._insert(data, root.left)
            else:
                root.left = self._Node(data)
        if data > root.data:
            if root.right is not None:
                self._insert(data, root.right)
            else:
                root.right = self._Node(data)
        if root.data == data:
            raise ValueError(str(data) + " is already in the tree")
            

    def find(self, data):
        return self._find(data, self._root)
    
    # takes the root passed as an argument to compare it to the data that is looked for
    def _find(self, data, root):
        if root is None:
            return False
        if data < root.data:
            return self._find(data, root.left)
        if data > root.data:
            return self._find(data, root.right)
        if root.data == data:
            return True
    
    # iterates over the tree using inorder traversal
    def __iter__(self):
        stack_roots = Stack()
        current_node = self._root
        while not stack_roots.is_empty() or current_node is not None: 
            while current_node is not None:
                stack_roots.push(current_node)
                current_node = current_node.left
            current_node = stack_roots.pop()
            yield current_node.data
            current_node = current_node.right