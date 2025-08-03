from linked_lists.singly_linked_list import SinglyLinkedList
from stacks.stack import Stack
from trees.binary_search_tree import BinarySearchTree
from queues.queue import Queue

def test_sll():
    # test of the singly linked list
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print("sll lenght", len(sll), "=",sll)
    sll2 = SinglyLinkedList()
    sll2.append(4)
    sll2.append(5)
    sll2.append(6)
    print("sll2 lenght", len(sll2), " =", sll2)
    new_sll = sll + sll2
    print("sll + sll2 =", new_sll)
    print("sll, sll2 =", sll, sll2)
def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("stack lenght", len(stack), "=", stack)
    stack.pop()
    stack.pop()
    print("stack lenght", len(stack), "after popping twice = ", stack)
    stack.pop()
    if stack.is_empty():
        print("popped again and the stack now is empty")
        try: 
            stack.pop()
        except IndexError as e:
            print(e, ". Tried to pop again but couldn't because the stack is empty", sep = "")
def test_bst():
    bst = BinarySearchTree()
    node = bst._Node(1)
    node.right
    if bst.is_empty():
        print("new bst created. It's currently empty")
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    print("bst: \n", bst)
    if bst.find(1):
        print("1 found succesfully")
    if bst.find(7):
        print("7 found succesfully")
    if bst.find(2):
        print("2 found succesfully")
    if not bst.find(8):
        print("8 not found succesfully")
    print("bst length:", len(bst))
def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("queue lenght", len(queue), "=", queue)
    queue.dequeue()
    print("queue lenght", len(queue), "after dequeue = ", queue)
    queue.dequeue()
    print("queue lenght", len(queue), "after another dequeue = ", queue)
    queue2 = Queue()
    queue2.enqueue(5)
    queue2.enqueue(6)
    queue2.enqueue(7)
    queue2.enqueue(8)
    print("queue2 lenght", len(queue2), "=", queue2)
    print("queue + queue2 = ", queue + queue2)
    try:
        queue.dequeue()
        queue.dequeue()
        print("queue was dequeued twice, now it's empty")
        queue.dequeue()
    except IndexError as e:
        print(e, ". Tried to dequeue again but couldn't because queue is empty", sep = "")

def main():
    test_sll()
    test_stack()
    test_bst()
    test_queue()
if __name__ == "__main__":
    main()