from singly_linked_list import Node, SinglyLinkedList


def print_reverse(sll: Node) -> None:
    if not sll:
        return

    if sll:
        print_reverse(sll.next)

    print(sll.data)


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(1, 6):
        ex.insert_at_end(i)

    print("=" * 80)
    print("The original List")
    ex.display()
    print("The reversed List")
    print_reverse(ex.head)
    print("=" * 80)
