from os.path import curdir

from singly_linked_list import SinglyLinkedList


def reverse_list(sll: SinglyLinkedList) -> None:
    print("Reversing List")
    current = sll.head
    if not current:
        return

    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    sll.head = prev


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(1, 7):
        ex.insert_at_end(i)
    ex.display()

    reverse_list(ex)
    ex.display()
