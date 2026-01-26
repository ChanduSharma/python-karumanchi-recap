from typing import Generic, TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head = None

    def display(self) -> None:
        start = self.head
        while start:
            print(start.data)
            start = start.next
        print("Display Done.")

    def insert_at_beg(self, value: T) -> None:
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def insert_at_end(self, value: T) -> None:
        current = self.head
        while current and current.next:
            current = current.next

        if current:
            new_node = Node(value)
            current.next = new_node
            new_node.prev = current
        else:
            self.insert_at_beg(value)

    def insert_at_pos(self, value: T, pos: int) -> None:
        if pos == 0:
            self.insert_at_beg(value)
        else:
            current = self.head
            cur_pos = 0
            while current and current.next and cur_pos < pos:
                current = current.next
                cur_pos += 1

            if cur_pos == pos and current:
                new_node = Node(value)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
            else:
                print(
                    f"Position {pos} does not exist as current length is only {cur_pos}"
                )


if __name__ == "__main__":
    d = DoublyLinkedList[int]()
    for i in range(5, 0, -1):
        d.insert_at_beg(i)
    d.display()
    d.insert_at_end(6)
    d.display()
    d.insert_at_pos(6, 3)
    d.display()
