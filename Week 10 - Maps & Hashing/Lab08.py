"""
PROBLEM STATEMENT :
In today’s Lab we will explore ways to design a Queue with O(1) lookup time
of the Maximum element. You must implement this design using the Deque.
URL reference here:
https://docs.python.org/3/library/collections.html#collections.deque
You will solve the problem as stated below:
Solution Hint :
Here you will Maintain two Queues - a Main Queue and a Queue holding the
Maximum value(s) from the Main Queue (AKA Max Queue). The Main Queue
contains the elements. The Max Queue contains the elements with Maximum
value. The Max Queue would have to be a double ended Queue as you would
like to be able to remove elements from both ends.
Example :
Let’s say we have the following:
We add an integer 1 into our Main Queue and I hope it is really obvious that
when the Main Queue contains a single element, the Max Queue can be populated without confusion :)
Main Queue: 1 << front of Queue
Max Queue : 1 << front of Queue
Now, let’s say we insert a 4 into the Main Queue. the Main Queue will look as
follows:
Main Queue: 4 → 1 << front of Queue
In the Max Queue, we don’t need 1 anymore, since 1 can never be the Max
of this Queue now. So we remove 1 and insert 4.
Main Queue: 4 → 1 << front of Queue
Max Queue : 4 << front of Queue
Say we insert 2 into the Main Queue. We know 2 is not the Max, but it can be
the Max if we de-Queue 1 and 4 from the Queue. So, we insert it onto the Max
Queue:
Main Queue: 2 → 4 → 1 << front of Queue
Max Queue : 2 → 4 << front of Queue
Further, If we insert a 3 into the Main Queue, we can get rid of the 2 from the
Max Queue, because 2 can no longer be the Max of the Queue, even if 4 and 1
are de-Queued. In that case our Queues become:
Main Queue: 3 → 2 → 4 → 1 << front of Queue
Max Queue : 3 → 4 << front of Queue
In the process of inserting 3, we removed elements from the back of the Max
Queue until we found an element ≥ 3.
This is because elements < 3 could never be Max after 3 is inserted. What I
stated above is exactly the algorithm for inserting an element in the Max Queue.
To lookup the Maximum Value (AKA Max), we just check the front of the Max
Queue which ensures O(1) lookup time.
While de-queuing elements, we check if they are equal to the front of the Max
Queue,and if so, we de-Queue from the Max Queue too. For example, after de-queuing 1, lets say we want to de-Queue 4. We see that 4 is the front of the
Max Queue, so we remove both the 4s. This does indeed make sense as 4 can
no longer remain the Maximum after it is removed from the Main Queue.
If the process described above is followed and you code up the example provided
we end up with the complexity stated below.
Time Complexity of lookup on the Max Queue: O(1)
Space Complexity on the Max Queue : O(n)
Submissions that don’t meet the mentioned Time and Space complexities will
have 50% credit taken off.
Very Very Important :
(1) Your code should be well commented which explains all the steps you are
performing to solve the problem. A submission without code comments
will immediately be deducted 15 points !
(2) As a comment in your code, please write your test-cases on how you would
test your solution assumptions and hence your code.
A submission without test cases (as comments) will immediately be deducted 15 points ! Please Remember : Although, written as comments -
You will address your test cases in the form of code and not prose 
"""
# Import deque from collections
from collections import deque

class MaxQueue:
    # Initialize the mainQueue and maxQueue
    def __init__(self):
        self.mainQueue = deque()
        self.maxQueue = deque()
    # Insert the value into the mainQueue
    def insert(self, value):
        # Append the value to the mainQueue
        self.mainQueue.append(value)
        # Check if the maxQueue is not empty and the last value in the maxQueue is less than the value
        while self.maxQueue and self.maxQueue[-1] < value:
            # Remove the last value from the maxQueue
            self.maxQueue.pop()
        self.maxQueue.append(value)
    # Remove the value from the mainQueue
    def remove(self):
        # Check if the mainQueue is empty
        if self.mainQueue[0] == self.maxQueue[0]:
            # Remove the value from the maxQueue from the left
            self.maxQueue.popleft()
        # Remove the value from the mainQueue from the left
        self.mainQueue.popleft()
    # Get the maximum value from the maxQueue 
    def getMax(self):
        return self.maxQueue[0]
    # Print the mainQueue
    def printMainQueue(self):
        return self.mainQueue
    # Print the maxQueue   
    def printMaxQueue(self):
        print(self.maxQueue)
        
# Test Cases
maxQueue = MaxQueue()
maxQueue.insert(1)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

maxQueue.insert(4)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

maxQueue.insert(2)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

maxQueue.insert(3)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

maxQueue.insert(5)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

maxQueue.remove()
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

# Null Test Case
maxQueue = MaxQueue()
try:
    maxQueue.remove()
except Exception as e:
    print(f"Error occurred: {e}")
print(f"Main Queue: {maxQueue.printMainQueue()}")
try:
    print(f"Max Queue: {maxQueue.getMax()}")
except Exception as e:
    print(f"Error occurred: {e}")
    
# 1 element Test Case
maxQueue = MaxQueue()
maxQueue.insert(1)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")

# 2 copies of the same element Test Case
maxQueue = MaxQueue()
maxQueue.insert(1)
maxQueue.insert(1)
print(f"Main Queue: {maxQueue.printMainQueue()}")
print(f"Max Queue: {maxQueue.getMax()}")
