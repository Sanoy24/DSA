class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def __str__(self):
        values = []
        temp = self.top
        while temp:
            value = values.append(str(temp.value))
            temp = temp.next
        return "->".join(values) if values else "Empty"

    def push(self, value):
        if value is None:
            raise ValueError("Cannot push None to stack")
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value  # removed value


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print("Initial stack:", my_stack)
print("Popped:", my_stack.pop())
print("After popping:", my_stack)
