<<<<<<< HEAD
A = [50, 11, 33, 21, 40, 50, 40, 40, 21]
j,low = 0,0
i = low - 1
high = len(A)-1 #pivot is last element
'''
partition for (j=low; j <= high-1, j++) #j incrememnt by 1
    if A[j] < pivot:
        i = i + 1 #increment, i at 10
        swap(A[i], A[j]) 
    }

}//for loop ends 
swap(A[i+1],A[high])
return i + 1

'''
#output: [10,30,40,50,70,90,80]#pivot is 70, where left is sorted and right isn't. run recursively on right/left
#pivot is always in correct index position
#half a runtime (recursion) is log2(n), overall: O(n*log2(n)) [+ o(n)]. average case.
#where O(n) is linear time median. worst case is o(nlog(n) #only if pivot is median

A_prime = [10,9,7,5,3,2,1] #input, quicksort. use code above. 
#pivot is 1. 
#worst case is O(n^2) ; running partition n times: nxn
=======
'''
Jan 8 to Feb 12 content is on the midterm

Time and space complexity will be on the midterm. Regarding how you should code the solution.

Given:  71, 72, 74, 73
        [0] [1] [2] [3]
        
Longest increasing subsequence: 71, 72, 73 | 71, 72, 74 -> length = 3

memo[3] = 1
memo[2] = 1
memo[1] = max(1, 1+memo[0], 1+memo[2]) = max(1, 1+1, 1+1) = max(1, 2, 2) = 2
memo[0] = max(1, 1+memo[1], 1+memo[2], 1+memo[3]) = max(1, 1+2, 1+1, 1+1) = max(1, 3, 2, 2) = 3
'''

# Time complexity: O(n^2)
def memorization(array):
    # Base case
    if len(array) == 0:
        return 0
    # Create a list of the same length as the array
    # and fill it with 1's
    memo = [1] * len(array)
    # Iterate through the array
    for i in range(1, len(array)):
        # Iterate through the array again
        for j in range(0, i):
            # If the current element is greater than the previous
            # and the memo[i] is less than memo[j] + 1
            if array[i] > array[j] and memo[i] < memo[j] + 1:
                # Set memo[i] to memo[j]   + 1
                memo[i] = memo[j] + 1
    # Return the maximum value in memo
    return max(memo)

array = [71, 72, 74, 73]
print(memorization(array)) # 3

# Space complexity: O(n)

"""
Simulation of the memorization function
array = [71, 72, 74, 73]
memo = [1, 1, 1, 1]

i, j = 0

i, j = 1, 0
array[1] > array[0] and memo[1] < memo[0] + 1 = 72 > 71 and 1 < 1 + 1
memo[1] = 1 + 1 = 2 
"""
>>>>>>> 7606802a444daaf94de83c5f2598519707e8b2f6
