class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class Binarysearchtree:
    def __init__(self):
        self.root = None#to create an empty tree

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if temp.value == new_node.value:
                return False #we dont take duplicates
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
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
                
                

                
   
b1 = Binarysearchtree()
b1.insert(10)
b1.insert(20)
b1.insert(5)

print(b1.root.value)
print(b1.root.left.value)
print(b1.root.right.value)
print(b1.contain(6))


        