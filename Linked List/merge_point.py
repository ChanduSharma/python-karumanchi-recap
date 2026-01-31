from singly_linked_list import SinglyLinkedList


def find_merge_point(sll1, sll2):
    t = sll1.head
    c1 = 0
    while t:
        c1 += 1
        t = t.next

    t = sll2.head
    c2 = 0
    while t:
        c2 += 1
        t = t.next

    diff = c1 - c2 if c1 > c2 else c2 - c1

    if c1 > c2:
        t = sll1.head
        o = sll2.head
    else:
        t = sll2.head
        o = sll1.head

    while diff:
        t = t.next
        diff -= 1

    while t.data != o.data:
        t = t.next
        o = o.next

    return t.data if t else None


if __name__ == "__main__":
    ex1 = SinglyLinkedList[int]()
    ex2 = SinglyLinkedList[int]()
    ex3 = SinglyLinkedList[int]()

    for i in range(5):
        ex1.insert_at_end(i)
        ex2.insert_at_end(i + 5)
        ex3.insert_at_end(i + 11)

    ex2.insert_at_end(45)
    test = ex1.head
    while test.next:
        test = test.next

    test1 = ex2.head
    while test1.next:
        test1 = test1.next

    test.next = ex3.head
    test1.next = ex3.head

    print(f"Merge Point {find_merge_point(ex1, ex2)}")
