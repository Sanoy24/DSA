class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=0):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # ###############################################################################################################
    # Find Middle Node ( Interview Question)                                                                        #
    # Instructions                                                                                                  #
    # Implement the find_middle_node method for the LinkedList class.                                               #
    #
    # Note: this LinkedList implementation does not have a length member variable.                                  #
    #
    # If the linked list has an even number of nodes, return the first                                              #
    # node of the second half of the list.                                                                          #
    #
    # Keep in mind the following requirements:                                                                      #
    #
    # The method should use a two-pointer approach, where one pointer (slow) moves one                              #
    # node at a time and the other pointer (fast) moves two nodes at a time.                                        #
    #
    # When the fast pointer reaches the end of the list or has no next node, the slow pointer                       #
    # should be at the middle node of the list.                                                                     #
    #
    # The method should return the middle node when the number of nodes is odd or the first node                    #
    # of the second half of the list if the list has an even number of nodes.                                       #
    #
    # The method should only traverse the linked list once.  In other words, you can only use one loop.             #
    #################################################################################################################
    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def partition_list(self, x):
        if not self.head:
            return None
        dummy_one = Node(0)
        dummy_two = Node(0)

        before = dummy_one
        after = dummy_two
        current = self.head
        while current:
            if current < x:
                before.next = current
                before = current
            else:
                after.next = current
                after = current
            current = current.next
        before.next = None
        after.next = None
        before.next = dummy_two.next
        self.head = dummy_one.next
        return dummy_one.next

    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head

        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current

            current = current.next

    def get_decimal_value(self):
        dec = 0
        current = self.head
        while current:
            dec = (dec << 1) | current.value
            current = current.next
        return dec

    def reverse_between(self, start_index, end_index):
        dummy_node = Node(0)
        prev_node = dummy_node
        dummy_node.next = self.head
        for _ in range(start_index):
            prev_node = prev_node.next
        current_node = prev_node.next
        for _ in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = prev_node.next
            prev_node.next = node_to_move
        self.head = dummy_node.next


def find_kth_from_end(ll: LinkedList, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


# Problem: Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


def addTwoNumbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    dummy = Node(0)
    current = dummy
    carry = 0
    node1 = l1.head
    node2 = l2.head

    while node1 or node2 or carry:
        num1 = node1.value if node1 else 0
        num2 = node2.value if node2 else 0
        total = num1 + num2 + carry
        carry = total // 10
        digit = total % 10
        print("----------------------")
        print("carry: ", carry)
        print("digit: ", digit)
        print("-----------------------")
        current.next = Node(digit)
        current = current.next
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    result = LinkedList(0)
    result.head = dummy.next
    result.tail = current
    result.length = 0
    temp = result.head
    while temp:
        result.length += 1
        if not temp.next:
            result.tail = temp
        temp = temp.next

    return result


# my_linked_list.append(2)
# my_linked_list.append(3)

# my_linked_list.append(4)
# my_linked_list.append(5)
# # print(my_linked_list.pop_first())
# print("----Before reverse ----")
# my_linked_list.print_list()
# print("---After reverse--------")
# my_linked_list.reverse()
# my_linked_list.print_list()
# print(find_kth_from_end(my_linked_list, 2).value)

# for value in [2, 3, 4, 5]:
#     my_linked_list.append(value)

# my_linked_list.reverse_between(1, 3)
# my_linked_list.print_list()

linked_list_one = LinkedList(6)
linked_list_two = LinkedList(8)
linked_list_one.append(6)
linked_list_one.append(8)

linked_list_two.append(8)
linked_list_two.append(9)

# 6->6->8
# 8->8->9

#   866
# + 988
# ------


# 342 + 543

# l1 = 2->4->3->None
# l2 = 3->4->5->None

print(addTwoNumbers(linked_list_one, linked_list_two).print_list())
