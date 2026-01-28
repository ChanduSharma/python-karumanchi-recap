from typing import Generic, TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, data, next=None):
        self.data = data
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


class CircularLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data)
            if current.next == self.head:
                break
            current = current.next
        print("Display Done")

    def insert_at_beg(self, value: T) -> None:
        new_node = Node(value)
        new_node.next = new_node
        current = self.head
        while current and current.next != self.head:
            current = current.next

        if not current:
            self.head = new_node
        else:
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, value: T) -> None:
        current = self.head

        while current and current.next != self.head:
            current = current.next

        if not current:
            self.insert_at_beg(value)
        else:
            new_node = Node(value)
            current.next = new_node
            new_node.next = self.head

    def del_at_beg(self) -> None:
        current = self.head

        if not self.head:
            return

        while current and current.next != self.head:
            current = current.next

        if current is self.head:  # means single element
            self.head = None
        else:
            current.next = self.head.next
            self.head = self.head.next

    def del_at_end(self) -> None:
        if not self.head:
            return

        if self.head is self.head.next:
            self.head = None
            return

        current = self.head
        previous = self.head

        while current and current.next != self.head:
            previous = current
            current = current.next

        previous.next = self.head


if __name__ == "__main__":
    ex = CircularLinkedList[int]()
    for i in range(4, -1, -1):
        ex.insert_at_beg(i)
    ex.display()
    ex.insert_at_end(5)
    ex.display()
    ex.del_at_beg()
    ex.display()
    ex.del_at_end()
    ex.display()
