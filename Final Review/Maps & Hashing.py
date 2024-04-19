from collections import deque

class max_Queue:
    def __init__(self):
        self.mainQueue = deque()
        self.maxQueue = deque()
        
    def add(self, value):
        self.mainQueue.append(value)
        
        while self.maxQueue and self.maxQueue[-1] < value:
            self.maxQueue.pop()
        self.maxQueue.append(value)
        
    def remove(self):
        if self.mainQueue[0] == self.maxQueue[0]:
            self.maxQueue.popleft()
        self.mainQueue.popleft()
        
    def MAX(self):
        return self.maxQueue[0]
    
    def printMainQueue(self):
        return self.mainQueue 
    
    def printMAxQueue(self):
        return self.maxQueue
    
maxQueue = max_Queue()
maxQueue.add(1)
maxQueue.add(4)
print(maxQueue.printMainQueue())
print(maxQueue.MAX())
maxQueue.add(2)
maxQueue.add(3)
print(maxQueue.printMainQueue())
print(maxQueue.MAX())