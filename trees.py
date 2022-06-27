class Node:#creating how the node should appear
    def __init__(self,value):
        self.value=value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None#creaqting an empty tree

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
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
                    return  True
                temp = temp.right
            
                
            
        
        



        
my_tree = BinarySearchTree()#creating an object
my_tree.insert(10)
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(11)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)


