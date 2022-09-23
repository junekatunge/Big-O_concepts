class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linked_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next
            
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.length = 1
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return False
        if self.length == 1:
            self.head = None
            self.length -= 1
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
    
    
n1 = Linked_list(7)

n1.append(8)
n1.append(4)
n1.append(3)
n1.append(3)
n1.pop()

n1.print_list()  
