from linked_lists.singly_linked_list import SinglyLinkedList
def main():
    #test of the singly linked list
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print("sll =",sll)
    sll2 = SinglyLinkedList()
    sll2.append(4)
    sll2.append(5)
    sll2.append(6)
    print("sll2 =", sll2)
    new_sll = sll + sll2
    print("new sll =", new_sll)
    print(sll, sll2)
if __name__ == "__main__":
    main()