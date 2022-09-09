#we want create a node
from ast import Not
from operator import ne
from re import L
from tkinter import N


class Node:
    def __init__(self,value):
        self.value =value
        self.next = None 
#we create a class for a list      
class Linkedlist:
    def __init__(self,value):#function of a constructor is to assign values to object when an object is created here a node is created
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
#we create a function for printing a list        
    def print_list(self):
        temp = self.head
        while temp is not None:      #this will iterate until the condition is false   #mbaka saa kumi
            print(temp.value)
            #then we move to the next value
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:    
            pre = self.tail
            #now we introduce the new node
            pre.next = new_node
            #then assign pre to the new node
            pre = new_node
            #the new node becomes the last node then we move the tail to the new node
            self.tail =pre
            self.length +=1
            
  #note: inorder to move head and tail we assign new nodes
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:    
            temp = new_node
            temp.next = self.head
            self.head = temp
        self.length +=1

        
    def pop_first(self):
        #if the length is zero nothing in the list
        if self.length == 0:
            self.head = None
            self.tail = None
            return None
        if self.length > 0:
            self.head = self.head.next
        if self.length == 1:
            self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
            return None
    
    # def pop(self):#remove the last element in the list
    #     if self.length == 0:
    #         return None
    #     while self.length is not None:#as long as length is noot none then iteration through the list will occur
    #         temp = self.head
    #         temp.next = temp
    #     temp.next = None
    #     temp = None
        
    #pop removing the last element
        
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.head.next
            self.head = None
        pre = self.head
        temp = self.head
        pre = temp
        while (temp.next) is not None:
            temp = temp.next
        temp = self.tail
        self.tail = pre
        temp = None
        
    def get_value(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):#iterate through the list until the value at the particular index is found
                temp = temp.next
            return temp.value
            
        
    def reverse(self):
        pre = self.head
        self.head = self.tail
        self.tail = pre
        after = pre.next
        before = None
        for _ in range(self.length):
            after=pre.next
            pre.next = before
            before = pre
            pre = after
    #finding the middle value
    def get_middle_value(self):
        middle_value = self.length//2
        pre=self.head
        if middle_value is not True:
            pre= pre.next
        return pre.value
    #prepend        
    def insert_node(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else: 
            pre = new_node
            pre.next = self.head
            self.head = pre
        self.length +=1
   
   #delete first element in a list     
    def delete_first(self):
        if self.length == 0:#invalid
            return None
        else:
            self.head = self.head.next
        
    #remove item:
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 1:
            self.head = None
            
        pre = self.get_value(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        return temp.value 
    
    def remove(self,index):
        if index < 0  or index >= self.length:
            return None
        if self.length == 1:
            self.head = None
            
        
        
        
                
              
            
            
       
    
                
       
            

LinkedlistA = Linkedlist(7)             
LinkedlistA.append(8)
LinkedlistA.append(9)
LinkedlistA.prepend(6)
#LinkedlistA.insert_node(1)
#LinkedlistA.delete_first()
LinkedlistA.remove(8)
#print(LinkedlistA.get_value(2))
#LinkedlistA.reverse()
#LinkedlistA.pop()
#LinkedlistA.pop_first()#pop the first item
#LinkedlistA.pop_first()#pop the second item
#LinkedlistA.pop_first()#pop the 3rd item
#print(LinkedlistA.get_middle_value())

LinkedlistA.print_list()
