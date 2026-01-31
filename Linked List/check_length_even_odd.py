from singly_linked_list import Node, SinglyLinkedList


def is_length_even(sll: SinglyLinkedList) -> int:
    if not sll:
        return 0

    current = sll.head

    if current and not current.next:
        return 0

    while current and current.next:
        current = current.next.next
        if not current:
            return 1

    return 0


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(1, 6):
        ex.insert_at_end(i)

    print(f"Is List even Length: {is_length_even(ex)}")
