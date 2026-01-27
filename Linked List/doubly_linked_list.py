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

    # Insertion methods
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
                print(f"Position {pos} does not exist. Length: {cur_pos}")

    # Deletion methods
    def del_at_beg(self) -> None:
        if self.head:
            self.head = self.head.next
            self.head.prev = None

    def del_at_end(self) -> None:
        current = self.head
        while current and current.next:
            current = current.next

        if current and current.prev:
            current.prev.next = None
        else:
            # if current.prev is None means it's head node
            # or if current is None means there is no node
            self.head = None

    def del_at_pos(self, pos: int) -> None:
        if pos == 0:
            self.del_at_beg()
        else:
            current_position = 0
            current = self.head

            while current and current.next and current_position < pos:
                current = current.next
                current_position += 1

            if current and current_position == pos:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                current.next = None
                current.prev = None
            else:
                print(f"Position {pos} does not exist. Length: {current_position}")


if __name__ == "__main__":
    d = DoublyLinkedList[int]()
    for i in range(5, 0, -1):
        d.insert_at_beg(i)
    d.display()
    d.insert_at_end(7)
    d.display()
    d.insert_at_pos(6, 0)
    d.insert_at_pos(6, 6)
    d.display()
    d.del_at_beg()
    d.display()
    d.del_at_end()
    d.display()
