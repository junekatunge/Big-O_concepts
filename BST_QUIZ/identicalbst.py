class Node:
    def __init__(self,value = 1):
        self.value = value
        self.left = None
        self.right = None
        # self.left.left = 3
        # self.right.right = 3
class Binarytree:
    def __init__(self):
        self.root = None
       
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        # if its not none
        temp = self.root
        while(True):#loop thru until every value is inserted
            if temp.value == new_node.value:
                return False#we dont take duplicates
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # if its not none
                temp = temp.left
            else:
                if new_node.value > temp.value:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
                        
    def identical(self):
        temp = self.root
        pre = self.root
        
        while temp.left is not None:
            while pre.right is not None:
                temp = temp.left
                pre = pre.right
                if temp.value == pre.value:
                    return "identical"
                
                    # if temp is not None and pre is not None:
                    #     temp = temp.left
                    #     pre = pre.right
                    #     if temp.value == pre.value:
                    #         return "they are identical"
                        
                        
                    
                        
                        
                        
                    
b1 = Binarytree()
b1.insert(1)
b1.insert(0)
b1.insert(2)


# print(b1.root.value)
# print(b1.root.left.value)
# print(b1.root.right.value)
print(b1.identical())
        

                    
            
            
            
                
            