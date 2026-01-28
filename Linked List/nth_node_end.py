from singly_linked_list import SinglyLinkedList


def nth_node_from_end(sll, n):
    count = 1
    temp = sll.head
    while count < n and temp is not None:
        count += 1
        temp = temp.next

    if count < n or temp is None:
        return

    nth = sll.head
    while temp.next:
        nth = nth.next
        temp = temp.next

    return nth.data


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(1, 100):
        ex.insert_at_end(i)
    ex.display()

    n = 3
    result = nth_node_from_end(ex, n)
    print(f"Nth node from end: {result}")
