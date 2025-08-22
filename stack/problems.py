"""
Create a constructor for Class Stack that implements
a new stack with an empty list called stack_list.
"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


"""
The reverse_string function takes a single parameter string, which is the string
you want to reverse.

Return a new string with the letters in reverse order.
"""


def reverse_string(string: str) -> str:
    stack = Stack()
    reversed_string = ""
    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


"""
The sort_stack function takes a single argument, a Stack object.
The function should sort the elements in the stack in ascending 
order (the lowest value will be at the top of the stack)
using only one additional stack. 

"""


def sort_stack(stack: Stack):
    _nstack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not _nstack.is_empty() and _nstack.peek() > temp:
            stack.push(_nstack.pop())
        _nstack.push(temp)
    while not _nstack.is_empty():
        stack.push(_nstack.pop())


# new_stack = Stack()
# new_stack.push(1)
# new_stack.push(2)
# new_stack.push(3)
# new_stack.push(4)
# new_stack.push(5)

# print("-----------before--------")
# print(new_stack)
# print("------pop last element--------")
# print(new_stack.pop())
# print(new_stack.pop())
# print("---------------after poppping")
# print(new_stack)

# print(reverse_string("YONAS"))


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()
