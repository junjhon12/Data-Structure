'''
Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.
Why call itself?
- To solve a problem by breaking it into smaller problems of the same form

Base case
- A condition that causes the recursion to stop

Recursive case
- A condition that causes the recursion to continue

Fibonacci sequence
- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...
Fibonacci formula (recursive) 
- fib(n) = fib(n-1) + fib(n-2)

n = 5

                        F(5)
                    /         \
                F(4)            F(3)
                /     \          /     \
            F(3)      F(2)     F(2)    F(1)
            /   \     /   \    /   \
        F(2)   F(1) F(1) F(0) F(1) F(0)
        /   \
    F(1)   F(0) 
    
    
    Problem (1): Climbing Stairs n = 5
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
                                            1
                                        |        |
                                        2        3
                                    |       |       |   
                                    3       4       5               Number higher than 5
                                |       |       |                  will Fall off (F) and discontinued
                                4       5       F       
                            |       |                     
                            5       F                     
                            
                      
'''

def fibonacci(n):
    if n > 20:  # stop if the number is higher than 20
        return None
    elif n == 0: # base case
        return 0
    elif n == 1: # base case
        return 1
    else: # recursive case
        return (fibonacci(n-1) + fibonacci(n-2))

    
    
n = 5
print(fibonacci(n))











































