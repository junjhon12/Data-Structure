"""
Below is how the arrays are represented
ARRAY1[] = [1, 6, 9, 10, 11, 21]
Here length of ARRAY1 is m.
ARRAY2[] = [2, 6, 9, 11, 17, 21]
Here length of ARRAY2 is n.
The output array to be returned would be:
ARRAY[] = [6, 9, 11, 21]
ATTN : Please be reminded that you cannot use library functions to do any of
the tasks required above. Doing so would straight up result in a score of Zero !
You will solve the problem in three ways:-
(1) [40 points] Implement the function in such a way that your solution solves
the problem with O(mn) time complexity. O(mn) is same as O(m ∗ n).
This brute-force method suggested has a name called ”loop-join” where
you basically just traverse through the elements of one array comparing
it to the elements of the other array.
(2) [40 points] In a separate implementation, code up a solution in such a way
that your solution solves the problem with O(nlog(m)) time complexity
2
or O(mlog(n)) time complexity. Here log means to the base of 2. I’m sure
you already know that the hint is to use Binary Search.
(3) [20 points] In a separate implementation, code up a solution in such a
way that your solution can run linearly with O(m + n) ≈ O(N) time
complexity.
"""
# O(n^2) BRUTE_FORCE
def loop_join(array1, array2):
    joined_array = []
    i = 0
    j = 0
    while len(array1) > i and len(array2) > j:
        if array1[i] == array2[j]:
            joined_array.append(array1[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return joined_array

array1 = [1, 6, 9, 10, 11, 21]
array2 = [2, 6, 9, 11, 17, 21]
print(loop_join(array1, array2))

# O(nlog(m))
def loop_join(array1, array2):
    joined_array = []
    if len(array1) < len(array2):
        array1, array2 = array2, array1
    unique = set(array1)
    for i in array2:
        if i in unique and i not in joined_array:
            joined_array.append(i)
    return joined_array

print(loop_join(array1, array2))

# O(m+n)
def loop_join(array1, array2):
    joined_array = []
    i, j = 0, 0
    while len(array1) > 1 and len(array2) > j:
        if array1[i] == array2[j]:
            if len(joined_array) == 0 or array1[i] != joined_array[-1]:
                joined_array.append(array1[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return joined_array

print(loop_join(array1, array2))

"""
Lab 2:
You are given an array of integers and an index x.
Without sorting Re-arrange the array as below:
elements less than array[x], followed by elements equal to array[x], followed by elements greater than array[x]
Array, a = [3,5,2,6,8,4,4,6,4,4,3] and x = 5
Write a Python Program that re-arranges the above given array exactly
as shown below without using a sorting routine of any kind
output array = [3,2,3,4,4,4,4,5,6,8,6]
Here You are allowed to use an extra array to solve the problem.

You are given an array of integers and an index x.
Without sorting Re-arrange the array as below:
elements less than array[x], followed by elements equal to array[x], followed by elements greater than array[x]
Array, a = [3,5,2,6,8,4,4,6,4,4,3] and x = 5
Write a Python Program that re-arranges the above given array exactly
as shown below without using a sorting routine of any kind
output array = [3,2,3,4,4,4,4,5,6,8,6]
"""
# Sorting with extra array
def rearranging(array, target):
    low = []
    equal = []
    high = []
    for i in array:
        if i < array[target]:
            low.append(i)
        elif i == array[target]:
            equal.append(i)
        else:
            high.append(i)
    return low + equal + high

array = [3,5,2,6,8,4,4,6,4,4,3]
target = 5
print(rearranging(array, target))

# Sorting without extra array : Iterative
def rearranging_Iterative(array, target):
    low = 0
    middle = 0
    high = len(array) - 1
    while middle <= high:
        if array[middle] < target:
            array[low], array[middle] = array[middle], array[low]
            low += 1
            middle += 1
        elif array[middle] > target:
            array[high], array[middle] = array[middle], array[high]
            high -= 1
        else:
            middle += 1
    return array

print(rearranging_Iterative(array, target))