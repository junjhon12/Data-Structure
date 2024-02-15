# Time complexity: O(n^2)
def intersection_lvl1(array1, array2):
    # Use a set to store the elements of the first array
    result = []
    m = 0 
    n = 0 
    # Check if the pointers are within the bounds of the arrays
    while m < len(array1) and n < len(array2):
        # If the elements are equal, add it to the result list
        if array1[m] == array2[n]:
            result.append(array1[m])
            m += 1
            n += 1
        # If the element in array1 is smaller, advance its pointer
        elif array1[m] < array2[n]:
            m += 1
        # If the element in array2 is smaller, advance its pointer
        else:
            n += 1
    return result

# Time complexity: O(nlogm)
def intersection_lvl2(arr1, arr2):
    # Create a list to store the result
    result = []
    # If the first array is shorter, swap the arrays
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    arr2.sort()  # Sorting the shorter array for binary search
    for num in arr1:
        # If the number is in the second array and not in the result list, add it to the result list
        if num in arr2 and num not in result:
            result.append(num)
    return result

# Time complexity: O(n + m)
def intersection_lvl3(arr1, arr2):
    # Create a list to store the result
    result = []
    i = 0
    j = 0
    # While the pointers are within the bounds of the arrays
    while i < len(arr1) and j < len(arr2):
        # If the elements are equal, add it to the result list
        if arr1[i] == arr2[j]:
            # If the result list is empty or the last element is not equal to the current element, add it to the result list
            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])
            i += 1
            j += 1
            # If the elements are not equal, advance the pointer of the smaller element
        elif arr1[i] < arr2[j]:
            i += 1
            # If the elements are not equal, advance the pointer of the smaller element
        else:
            j += 1
    return result

# Test cases

# Empty arrays
null1 = []
null2 = []
result = intersection_lvl1(null1, null2)
print(result)
result = intersection_lvl2(null1, null2)
print(result)
result = intersection_lvl3(null1, null2)
print(result)

# Identical arrays
identical1 = [1, 2, 3, 4, 5]
identical2 = [1, 2, 3, 4, 5]
result = intersection_lvl1(identical1, identical2)
print(result)
result = intersection_lvl2(identical1, identical2)
print(result)
result = intersection_lvl3(identical1, identical2)
print(result)

# Arrays with different lengths
diffLength1 = [3, 6, 9, 12, 15]
diffLength2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = intersection_lvl1(diffLength1, diffLength2)
print(result)
result = intersection_lvl2(diffLength1, diffLength2)
print(result)
result = intersection_lvl3(diffLength1, diffLength2)
print(result)

ARRAY1 = [1, 6, 9, 10, 11, 21]
ARRAY2 = [2, 6, 9, 11, 17, 21]
result = intersection_lvl1(ARRAY1, ARRAY2)
print(result)
result = intersection_lvl2(ARRAY1, ARRAY2)
print(result)
result = intersection_lvl3(ARRAY1, ARRAY2)
print(result)
