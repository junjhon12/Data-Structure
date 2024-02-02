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
                /     \          /     \                Time Complexity: O(2^n)
            F(3)      F(2)     F(2)    F(1)             Space Complexity: O(n)
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

    Time Complexity: O(2^n)
    Space Complexity: O(n)        
                            
                      
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

def climbStairs(n):
    if n > 20:  # stop if the number is higher than 20
        return None
    elif n == 0: # base case
        return 1
    elif n == 1: # base case
        return 1
    
    if n > 1:
        return climbStairs(n-1) + climbStairs(n-2)
    
n = 6
print(fibonacci(n))
print(climbStairs(n))

'''
Top Down Approach
                                                                         
_               n=6       1 way since we're already at the top             
#|_             n=5       1 way since we can only take 1 step
###|_           n=4       2 ways since we can take 1 step or 2 steps
#####|_         n=3       3 ways since we can take 1 step or 2 steps
#######|_       n=2       5 ways since we can take 1 step or 2 steps
#########|_     n=1       8 ways since we can take 1 step or 2 steps
###########|_   n=0       13 ways since we can take 1 step or 2 steps

Downstair Fibonacci Formula : F(n) = F(n-1) + F(n-2)

[Decryption]

A(1) F(6)  K(11) P(16) U(21) Z(26)
B(2) G(7)  L(12) Q(17) V(22)                            { Method 1: A(1)    B(2)    A(1)}
C(3) H(8)  M(13) R(18) W(23)            Example = '121' { Method 2: L(12)   A(1)        }> 3 ways
D(4) I(9)  N(14) S(19) X(24)                            { Method 3: A(1)    U(21)       }
E(5) J(10) O(15) T(20) Y(25)

Task: Given a string of numbers, return the number of ways it can be decrypted.

Example: '121' -> 3 ways
def decodeWays(s: str) -> int:
    if s[0] == '0':
        return 0
    if len(s) <= 1:
        return 1
    if int(s[:2]) <= 26:
        return decodeWays(s[1:]) + decodeWays(s[2:])
    else:
        return decodeWays(s[1:])
'''
'''
Professor's Solution:
def decoding(self, S str) -> int:       # -> will return the type of the output by using (-> int)
    D = {len(S) : 1}                    # D is a dictionary that stores the number of ways to decode the substring S[i:]
    def dec(i):                         # This function returns the number of ways to decode the substring S[i:]
        if s[i] == '0':                 # Base case
            return 0                    # Base case
        if i not in D:                  # If i is not in D, then store the number of ways to decode the substring S[i:]
            return D[i]                 # If i is in D, then return the number of ways to decode the substring S[i:]
        n_ways = dec(i+1)               # This is the number of ways to decode the substring S[i:]
        if i+1 < len(S) and (S[i] == '1' or (S[i] == '2' and S[i+1] < '7')):        # This checks if the substring S[i:] can be decoded
            s[i+1] == "1" or (s[i+1] == "2" and s[i+2] in "0123456")                # This also checks if the substring S[i:] can be decoded by checking the first two characters
                n_ways += 1                                                         # This increments the number of ways to decode the substring S[i:]
        D[i] = n_ways                                            # This stores the number of ways to decode the substring S[i:]
        return n_ways                                            # This returns the number of ways to decode the substring S[i:]
        
'''

def decode(s: str) -> int:
    decode_storage = dict() # This dictionary stores the number of ways to decode the substring S[i:]
    def num_decode(i): # This fuction returns number of ways to decode the substring S[i:]
        if i == len(s): # Check if the substring S[i:] is empty
            return 1
        if s[i] == '0': # Check if the first character of the substring S[i:] is 0
            return 0
        if i in decode_storage: # Check if i is in the dictionary
            return decode_storage[i]
        result = num_decode(i+1) 
        if i <= len(s) - 2 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')): # Check if the substring S[i:] can be decoded
            s[i+1] == "1" or (s[i+1] == "2" and s[i+2] in "0123456") 
            result += num_decode(i+2)
        decode_storage[i] = result # Store the number of ways to decode the substring S[i:]
        return result # Return the number of ways to decode the substring S[i:]
    return num_decode(0)  # Return the number of ways to decode the substring S[i:]

s = '121'
print(decode(s))  # Output: 3
# s = '0121' -> 0 since the first character is 0
# s = '1210' -> 2 since the last character is 0
# s = '1201' -> 1 since the second character is 0
# Having 0 in the string will cause act as a stopper