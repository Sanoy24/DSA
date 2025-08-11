class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
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


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.append(4)
my_linked_list.append(5)
# print(my_linked_list.pop_first())
print("----Before reverse ----")
my_linked_list.print_list()
print("---After reverse--------")
my_linked_list.reverse()
my_linked_list.print_list()
