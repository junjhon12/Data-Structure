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
                rightIndex = middleIndex - 1
        else:
            if target < array[middleIndex] or target > array[rightIndex]:
                rightIndex = middleIndex - 1
            else:
                leftIndex = middleIndex + 1
    return f'{target} not found in the array'

# ---------------------------------------------------------------------------------------------
array = [1,2,3,4,5,6,7,8,9,10]
target = 2
print(binarySearch_Lvl1(array, target))

# Simulating the binary search
# array = [1,2,3,4,5]
# target = 4
# leftIndex = 0 (1), rightIndex = 4 (5)
# middleIndex = 0 + (4 - 0) // 2 = 2 (3)
# if (4 == 3) -> False
# elif (4 < 3) -> False
# else (4 > 3) -> True
# leftIndex = middleIndex + 1 = 3 (4)
# search between [4, 5]
# middleIndex = 3 + (4 - 3) // 2 = 3 (4)
# if (4 == 4) -> True

array = [3,4,5,1,2]
target = 1
print(binarySearch_Lvl2(array, target))

# Simulating the binary search for rotated array
# array = [3,4,5,1,2]
# target = 1
# leftIndex = 0 (3), rightIndex = 4 (2) [3,4,5,1,2]
# middleIndex = 0 + (4 - 0) // 2 = 2 (5) []
# if (1 == 5) -> False
# elif (3 <= 5) -> True
#   if (1 > 5) or (1 < 3) -> True
#      leftIndex = middleIndex + 1 = 3 (1) [1,2]
# middelIndex = 3 + (4 - 3) // 2 = 3 (1) 
# if (1 == 1) -> True
# return f'Found {target} at index {middleIndex}' -> Found 1 at index 3