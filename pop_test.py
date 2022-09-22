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
    
n1 = Linked_list(7)
n1.print_list()  
n1.append(8)
