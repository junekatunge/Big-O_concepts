


class Node:
    def __init__(self,value):
        self.value= value
        self.next = None
class Linkedlist:#to create a linked list
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next
    
    def push_back(self,value):#append
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            pre = self.head
            while pre.next is not None:
                pre = pre.next
            pre.next = new_node
            self.length += 1
    
    def push_front(self,value):#prepend
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.length = 1
        else:
            pre = new_node
            pre.next = self.head
            self.head = pre
            self.length += 1
            
    def pop_back(self):#pop
        if self.length == 1:
            self.head = None
        else:
            pre = self.head
            while pre.next.next is not None:
                pre = pre.next.next
            pre.next = None
            self.length -= 1
            
    def top_front(self,index):#return the front item/get
       if index == self.length or index < 0:#check if there is an item in the list

           return None
       elif index == 0:
           print (self.head.value)
    
    def middle_value(self):
        middle_value = self.length // 2
        pre = self.head
        while pre is not middle_value:#if middle_value is not True:
            pre = pre.next
        print(pre.value)
     #find key?
    def find(self,index):
        if self.length == 0:
            return False
        elif index is True:
            return True
        else:
            return False 
        
       
           
        
                
            

LinkedlistA = Linkedlist(7) 
LinkedlistA.push_back(1)
LinkedlistA.push_back(4)
#LinkedlistA.push_front(5)
# LinkedlistA.pop_back()
# LinkedlistA.top_front(0)
#LinkedlistA.middle_value()
LinkedlistA.find(2)

LinkedlistA.print_list()         