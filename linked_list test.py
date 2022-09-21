class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_list(self,value):
        new_node = Node(value)
        temp = self.head
        temp.next = new_node
        self.length += 1
    def has_cycle(self):
        temp = self.head
        pre = self.head
        while temp.next.next is not None:
            temp=temp.next.next
            pre= temp.next
            if temp == pre:
                return 1
            return 0
            
            
        # if self.head.next is None:
        #     return None
        # # node=self.print_list()
        # if self.tail.next == self.head:
        #     return 1
        # return 0
L1 = Linkedlist(1)
L1.append_list(2)
L1.append_list(7)
L1.append_list(4)
L1.append_list(4)
print(L1.has_cycle())
L1.print_list()

        