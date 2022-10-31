# Implement Stack using Queues
class MyStack:

    def __init__(self):
        self.qu1 = deque()
        

    def push(self, x: int) -> None:
        self.qu1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.qu1)-1):
            self.push(self.qu1.popleft())#we pop from the left and return to the right
        return self.qu1.popleft()
        
        

    def top(self) -> int:
        return self.qu1[-1]
        

    def empty(self) -> bool:
        if len(self.qu1) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()