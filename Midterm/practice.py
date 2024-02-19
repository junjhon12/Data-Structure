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