"""
A Node for a linked list-based data structure.
"""


class Node:
    def __init__(self, value):
        """
        Creates a new Node instance.
        @param {*} value - The value to store in the node.
        """
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value=None):
        """
        Creates a new Queue instance.

        @param {*} [value=None] - An optional initial value to add to the queue.
        """
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
        """
        Returns a string representation of the queue.

        @returns {string} - A string showing the queue's elements, or "empty" if the queue is empty.
        """
        values = []
        temp = self.first
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return "->".join(values) if values else "Empty"

    def enqueue(self, value: int) -> None:
        """
        Adds a new node to the end of the queue.

        @param {number} value - The value to add.
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """
        Removes and returns the first node from the queue.

        @returns {number|null} - The value of the dequeued node, or null if the queue is empty.
        """
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
