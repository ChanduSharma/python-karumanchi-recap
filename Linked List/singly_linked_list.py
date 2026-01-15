import time
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


class SinglyLinkedList(Generic[T]):
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data: T) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: T) -> None:
        new_node = Node(data)
        current = self.head

        while current and current.next:
            current = current.next

        if current:
            current.next = new_node
        else:
            self.insert_at_beg(data)

    def insert_at_pos(self, data, pos=0) -> None:
        pass
        if pos == 0:
            self.insert_at_beg(data)
        else:
            # want to get to one position before
            # insertion pos or the pos ends
            current_pos = 1
            current = self.head

            while current and current.next and current_pos < pos:
                current_pos += 1
                current = current.next

            if current:
                remaining = current.next
                new_node = Node(data)
                new_node.next = remaining
                current.next = new_node
            else:
                self.insert_at_beg(data)

    def del_at_beg(self):
        print("Deleting the first node...")
        time.sleep(1)
        if self.head:
            self.head = self.head.next
        print("Deleted")

    def del_at_end(self):
        print("Deleting the last node...")
        time.sleep(1)
        if not self.head:  # No nodes just return
            return

        current = self.head
        previous = None
        while current and current.next:
            previous = current
            current = current.next

        if previous and current:
            previous.next = current.next
        else:
            self.del_at_beg()
        print("Deleted")

    def del_at_pos(self, pos):
        if not self.head:
            return

        if pos == 0:
            self.head = self.head.next
        else:
            previous = None
            current = self.head
            cur_pos = 0
            while current and current.next and cur_pos < pos:
                cur_pos += 1
                previous = current
                current = current.next

            if cur_pos == pos:
                previous.next = current.next

    def display(self) -> None:
        start = self.head
        while start:
            print(start.data)
            start = start.next
        print("Display Done.")


if __name__ == "__main__":
    ex = SinglyLinkedList[int]()
    for i in range(6, 0, -1):
        ex.insert_at_beg(i)
    ex.insert_at_pos(2.5, 2)
    ex.insert_at_end(7)
    ex.insert_at_end(8)
    ex.display()

    ex.del_at_beg()
    ex.display()

    ex.del_at_end()
    ex.display()
    print("deleting at pos 3")
    ex.del_at_pos(3)
    ex.display()
