from re import T
import re


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binaryserchtree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False #we dont take duplicates
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:#on the right side
                if temp.right is None:
                    temp.right = new_node
                    return True
                #iif its not none
                temp = temp.right
    
    def contain(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            if value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def minimum_node(self,current):
        # while current_node.left is not None:
        #     current_node = current_node.left
        # return current_node.value
        while current.left is not None:
            current = current.left
        return current.value

    
    def maximum_node(self,current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value
    
    def print_values(self):
        temp = self.root
        pre = self.root
        while temp is not None and pre is not None:
            print(temp.value, pre.value)
            temp = temp.left
            pre = pre.right
                
        return None
       
            
        
            
    
b1 = Binaryserchtree()
b1.insert(20)
b1.insert(70)
b1.insert(10)
b1.insert(7)
# print(b1.root.value)
# print(b1.root.left.left.value)
# print(b1.root.right.value)
# print(b1.contain(13))
# print(b1.minimum_node(b1.root))# b1.root=> where the current position is
# print(b1.minimum_node(b1.root.right))#the minimum on the right position
# print(b1.maximum_node(b1.root))
print(b1.print_values()) 
                
                
                
                
                
             
        