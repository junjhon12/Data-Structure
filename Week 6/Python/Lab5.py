"""
Given ARRAY[] = [50, 11, 33, 21, 40, 50, 40, 21, 40]
Expected output: ARRAY[] = [11, 21, 33, 40, 50]
"""
# sorting routine: Merge Sort
def mergeSort(array):
    # Base case
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    # Divide the array into two halves
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    # Merge the two halves
    return merge(left, right)

# Merge the two halves
def merge(left, right):
    result = []
    # i is for left half and j is for right half
    i = j = 0
    # Compare the elements in the left and right halves
    while i < len(left) and j < len(right):
        # If the left half is less than the right half
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # If the right half is less than the left half
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        # Duplicate elements are not added if left and right are equal
        else:
            i += 1
    result.extend(left[i:]) # Add the remaining elements in the left half
    result.extend(right[j:]) # Add the remaining elements in the right half
    return result
    
ARRAY = [50, 11, 33, 21, 40, 50, 40, 21, 40]
print(mergeSort(ARRAY))

# Test Cases
# Array is NULL
ARRAY = []
print(mergeSort(ARRAY))

# Array has one element
ARRAY = [1]
print(mergeSort(ARRAY))

# Array has identical elements
ARRAY = [1, 1, 1, 1, 1, 1, 1, 1]
print(mergeSort(ARRAY))

# Array is sorted backwards
ARRAY = [10,9,8,7,6,5,4,3,2,1]
print(mergeSort(ARRAY))

"""
The Time Complexity of mergeSort is O(nlogn)
The Space Complexity of mergeSort is O(n)

The Time Complexity of merge is O(n)
The Space Complexity of merge is O(n) 
"""