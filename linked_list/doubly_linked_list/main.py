class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        if self.head is None:
            return None
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next
            print()

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> None:
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> None:
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> None:
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp

    def set_value(self, index: int, value: int) -> None:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        if self.head is None:  # Empty list case
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        current = self.get(index)
        prev = current.prev
        new_node.next = current
        new_node.prev = prev
        prev.next = new_node
        current.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        if temp is None:  # Safety check for get method
            return None
        prev = temp.prev
        next_node = temp.next
        prev.next = next_node
        next_node.prev = prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print("DLL before remove():")
my_doubly_linked_list.print_list()

print("\nRemoved node:")
print(my_doubly_linked_list.remove(2).value)
print("DLL after remove() in middle:")
my_doubly_linked_list.print_list()

print("\nRemoved node:")
print(my_doubly_linked_list.remove(0).value)
print("DLL after remove() of first node:")
my_doubly_linked_list.print_list()

print("\nRemoved node:")
print(my_doubly_linked_list.remove(2).value)
print("DLL after remove() of last node:")
my_doubly_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""
