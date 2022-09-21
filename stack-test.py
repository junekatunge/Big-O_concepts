class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
    # def push(self,value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.top = new_node
    #         self.length += 1
    #     new_node.next = self.top
    #     self.top = new_node
    #     self.length += 1
    def pop(self):
        if self.length == 0:
            return False
        temp = self.top
        self.top = temp.next
        temp.next = None
    
    def game_pop(self,a,b):
       
        temp = self.top
        self.top = temp.next
        temp.next = None
        for i in a:
            for j in b:
                total = 0
                maxSum = 24
            while total < maxSum:
                self.pop() 
                sum = i + j
                total += sum
                
            return "you are disqualified your score is" , total
         
a = [1,2,3,4,5]
b = [6,7,8,9]                
s = Stack(8)
s.game_pop(a,b)
# a.push(2)
# a.push(3)
# a.push(4)
# a.push(5)
# b = Stack(6)
# a.push(6)
# a.push(7)
# a.push(8)
# a.push(9)
# game_pop(a,b)



    
        
            
    
       