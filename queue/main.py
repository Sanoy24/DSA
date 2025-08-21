class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def __str__(self):
        values = []
        temp = self.first
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return "->".join(values) if values else "Empty"

    def enqueue(self, value: int) -> None:
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        temp.next = None
        self.length -= 1
        return temp.value


my_queue = Queue()
print("Initial:", my_queue)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print("After enqueuing 1, 2, 3:", my_queue)
print("Dequeued:", my_queue.dequeue())
print("After dequeuing:", my_queue)
