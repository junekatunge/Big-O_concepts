


class Node:#creating how the node should appear
    def __init__(self,value):
        self.value=value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None#creaqting an empty tree

    def insert(self,value):
        new_node = Node(value)#to insert a new node
        if self.root == None:
            self.root = new_node
            return True
        #if there is a value at the root then assign temp to the root
        temp = self.root
        while (True):#we will loop forever until while is True i.e until insertion is fully done ie final true
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:#left
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contain(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False#temp is None
    
    def minimum_value(self,current):
        while current.left is not None:
            current = current.left
        return current.value#if current.left is None that means we have already found the least node
    
    def delete_value(self,value):
        if self.root == None:
            return False
        temp = self.root
        while (True):
            if value < temp.value:
                temp = temp.left
            if value > temp.right:
                temp = temp.right
            else:
                temp.DeleteValue
        return False
            
    
    
    
                
            
            
                
            
        
        



        
my_tree = BinarySearchTree()#creating an object
my_tree.insert(10)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(11)
my_tree.insert(7)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contain(3))
print(my_tree.contain(17))

print(my_tree.minimum_value(my_tree.root))#for the left side
print(my_tree.minimum_value(my_tree.root.right))#for the right side


