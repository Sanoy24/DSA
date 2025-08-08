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

linked_list = LinkedList(2)
print(linked_list.head.value)