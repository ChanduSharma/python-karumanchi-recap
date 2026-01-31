from singly_linked_list import SinglyLinkedList


def find_middle(sll: SinglyLinkedList) -> int | None:
    if not sll:
        return None

    fast_ptr = sll.head
    slow_ptr = sll.head

    while fast_ptr:
        fast_ptr = fast_ptr.next
        if not fast_ptr:
            return slow_ptr.data

        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next

    return slow_ptr.data


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(1, 7):
        ex.insert_at_end(i)

    result = find_middle(ex)
    print(f"Middle Point is: {result}")
