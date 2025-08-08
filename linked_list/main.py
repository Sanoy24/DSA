class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printNode(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next
    def append(self,value):
        if self.head ==None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


linked_list = LinkedList(2)
linked_list.append(3)
linked_list.append(4)
linked_list.printNode()