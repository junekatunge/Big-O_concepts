class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):#creating an empty tree
        self.root = None
    
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        # if the root is avail
        temp=self.root
        while temp is not None:
            if temp.value == new_node.value:
                return False#because you havent inserted anything
            if new_node.value < temp.value:
                temp.left = new_node
                return True
            elif new_node.value > temp.value:
                temp.right = new_node
                return True
        return False
    def contain(self,value):
        temp = self.root
        while temp is not None:#while the item is in the tree/while temp is still pointing to a node
            if value < temp.value:
                temp = temp.left
            if value > temp.value:
                temp = temp.right
            else:
                return True
        return False#if the item is not in the tree
            
        
                
my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(20)
my_tree.insert(8)
my_tree.insert(3)
my_tree.insert(9)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contain(10))
print(my_tree.contain(22))

            
        