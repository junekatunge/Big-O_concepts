# from email import header
# from hashlib import new
# from re import L


#from re import I


class Node:
    def __init__(self,value):#constructor method to initialize methods
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self,value):
        #create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 #after assigning the head and the tail to the node the length becomes 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next#move to the next node
            

    def append_list(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node    
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def pop(self):# if there is nothing in the list
        
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):#is not None
            pre =temp
            temp= temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1 #keep reducing the length to zero
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        #creating a new node
        new_node = Node(value)
        #there are two situations; when the list is empty and not empty(no node)and when a list has 1 node
         #first we assume that the list is empty 
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:#if have 1 item in a list
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        #3 sistuations when length is 0, length is 1 and when length is more 2 or more nodes
        #when length is zero
        if self.length == 0:
            return None
        if self.length == 1:#if the length is 2 nodes or more
            pre = self.head
            self.head =  self.head.next
            pre.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return pre
        
    def get_value(self,index):
        #check if the list is valid
        if index < 0 or index >= self.length:   #index is always less than the length
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def insert(self,index,value):#we want to insert a value at an index
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_list(value)
        #if you want to insert between a list
        new_node = Node(value)
        temp = self.get_value(index -1)#the index where the new value is going to be inserted minus one to get the previous index
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def set_value(self,index,value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False#if the list is invalid that is the index is not avaliable
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        #pop last
        if index == self.length -1:
            return self.pop()
        #otherwise if you want to remove from the middle
        pre= self.get_value(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp.value
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = None
            before = temp
            temp = after
        
    
            
            
    
            
            
            
        

    

LinkedlistA = Linkedlist(1)
#for testing append
LinkedlistA.append_list(2)
LinkedlistA.append_list(3)
LinkedlistA.append_list(4)
#for testing Prepend
#LinkedlistA.prepend(3)
#for setters    
#LinkedlistA.set_value(1,4)
#for inserting
#LinkedlistA.insert(1,1)
print(LinkedlistA.remove(2), '\n')#this will print out the node that is been removed

# LinkedlistA.reverse()
LinkedlistA.print_list()

#for getters
#print(LinkedlistA.get_value(2))
# For printing a new list
#print(LinkedlistA.head.value)
# #for testing pop
# print(LinkedlistA.pop())#print 2 items
# print(LinkedlistA.pop())#print 1 item
# print(LinkedlistA.pop())#print zero item




  