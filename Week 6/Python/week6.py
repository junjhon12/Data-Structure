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