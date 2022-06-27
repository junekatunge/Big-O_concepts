from curses.panel import top_panel


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
        def __init__(self,value):
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        
        def print_stack(self):
            temp = self.top
            while temp is not None:
                print (temp.value)
                temp = temp.next
        
        def push(self,value):
            new_node = Node(value)
            if self.height == 0:
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node
                
            self.height += 1 
        
        def pop(self):
            if self.height == 0:
                return None
            
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value   
            
                
                
                               
my_stack = Stack(4)
my_stack.push(1)
my_stack.push(17)
my_stack.push(21)
my_stack.push(100)
print(my_stack.pop())


my_stack.print_stack()
                