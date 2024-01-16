import math
# Monday : Binary Search Level 1
def binarySearch_Lvl1(array, target):
    leftIndex = 0
    rightIndex = len(array) - 1
    
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        
        if target == array[middleIndex]:
            return f'Found {target} at index {middleIndex}'
        elif target < array[middleIndex]:
            rightIndex = middleIndex - 1
        else:
            leftIndex = middleIndex + 1
    return f'{target} not found in the array'

# Tuesday : Binary Search Level 2 rotated array
def binarySearch_Lvl2(array, target):
    leftIndex = 0
    rightIndex = len(array) - 1
    
    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        
        if target == array[middleIndex]:
            return f'Found {target} at index {middleIndex}'
        elif array[leftIndex] <= array[middleIndex]:
            if target > array[middleIndex] or target < array[leftIndex]:
                leftIndex = middleIndex + 1
            else:
                left = mid + 1 # search right side
    return 'Not Found'

def find_Minumum (array):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif array[left] < array[mid]:
            if target > array[mid] or target < array[left]:
                left = mid + 1
                # search from the left side
                # If 
                while left <= right:
                    leftMid = left + (right - left) // 2
                    if target == array[leftMid]:
                        return leftMid
                    elif array[left] < array[leftMid]:
                        if target > array[leftMid] or target < array[left]:
                            left = leftMid + 1
                        else:
                            right = leftMid - 1
                    else:
                        if target < array[leftMid] or target > array[right]:
                            right = leftMid - 1
                        else:
                            left = leftMid + 1
            else:
                right = mid - 1
                



'''
b = [3, 9, 10, 11, 15, 19]  # sorted array
a = 16  # target value 
result = binary_search_Lvl1(a,b)
print(result)
b = []
a = 15  # target value
result2 = binary_search_Lvl1(a,b)
print(result2)
b = [15]
a = 15  # target value
result2 = binary_search_Lvl1(a,b)
print(result2)
'''

array = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
target = 2
result = binary_search_lvl2(target,array)
print(result)

# Wendesday problem
# Find the minimum value, not the index but the value without using a linear search using binary search
array = [320, 10000, 3823, 9524, 1]
