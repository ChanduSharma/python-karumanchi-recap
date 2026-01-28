from circular_linked_list import CircularLinkedList
from singly_linked_list import SinglyLinkedList


def check_if_cyclic(cll):
    slow_ptr = cll.head
    fast_ptr = cll.head

    while slow_ptr and fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
        if fast_ptr:
            fast_ptr = fast_ptr.next

        if slow_ptr is fast_ptr:
            return True

    return False


if __name__ == "__main__":
    ex = CircularLinkedList[int]()
    for i in range(5):
        ex.insert_at_end(i)
    ex.display()
    print(check_if_cyclic(ex))

    ex1 = SinglyLinkedList[int]()
    for i in range(9):
        ex1.insert_at_end(i)

    ex1.display()
    print(check_if_cyclic(ex1))
