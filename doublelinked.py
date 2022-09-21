

class Node:
    def __init__(self,value):
        # self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    #creating the first node
    def __init__(self):
        new_node = Node()
        self.head = new_node
        self.tail = new_node
        self.length = 1
    #read the values/reading from the list with the first node 
    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next
    #def append(self,value):
    def append(self,value):
        new_node = Node(value)
        #if self.head is None:
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else:
        
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            
        self.length -=1
        return temp.value
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.prev = None
            self.next = None
        else:
            new_node.next = self.head
            self.prev = new_node
            self.head = new_node
            new_node.prev = None
        self.length +=1
    def pop_first(self):
        pre = self.head
        if self.length == 0:
            return None
        else:
            self.head = self.head.next
            self.head.prev = None
            pre.next = None
            if self.length == 1:
                self.head = None
                self.tail = None
                self.prev = None
                self.next = None
                self.length -=1
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            if index < self.length/2:#meaning its in the first half
                for _ in range(index):
                    temp = temp.next
                
            #if index > self.length/2: second half
            else:
                temp = self.tail
                for _ in range(index,self.length -1,-1):
                    temp = self.prev
            return temp.value
            
    # def set(self,index,value):
    #     temp = self.get(index)
    #     if temp is not None:
    #         temp.value = value
    #         return True#that the values have been changed
    #     return False#when temp is None          
                
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)#then pass the value
        if index == self.length:
            return self.append(value)
        #if its inbetween a list
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next 
        new_node.prev = before
        new_node.next = after 

        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first(value)
        if index == self.length:
            return self.pop(value)
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        
        before.next = after
        after.prev = before
        
        temp.next = None
        temp.prev = None
        self.length -= 1
        return True    
            
            
        
        

DoubleLinkedListA = DoubleLinkedList(7)
DoubleLinkedListA.append(1)
DoubleLinkedListA.append(2)
DoubleLinkedListA.append(3)
DoubleLinkedListA.prepend(5)
#DoubleLinkedListA.set(0,4)
#DoubleLinkedListA.insert(3,4)
DoubleLinkedListA.remove(3,4)
#DoubleLinkedListA.pop_first()
#DoubleLinkedListA.get(0)
#DoubleLinkedListA.pop()
DoubleLinkedListA.print_list()
#print(DoubleLinkedListA.get(0))

        