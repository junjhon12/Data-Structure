# Binary search level 1
def BinarySearch_Lvl1(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return f'Found Target: {target} at index {mid}'
        elif array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
    return f'Target: {target} not found in array'

# Binary search level 2 roatated array
def BinarySearch_Lvl2(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = left + (right - left) // 2
        # Checks if target is at middle
        if target == middle:
            return f'Found Target: {target} at index {middle}'
        # Checks if left side is sorted
        elif array[left] <= array[middle]:
            if target > array[middle] or target < array[left]:
                # If not sorted, search right side
                left = middle + 1
            else:
                # If sorted, search left side
                right = middle - 1
        else:# Checks if right side is sorted
            if target < array[middle] or target > array[right]:
                # If not sorted, search left side
                left = middle - 1
            else:
                # If sorted, search right side
                right = middle + 1

array = [1,2,3,4,5,6,7,8,9,10]
target = 5
print(BinarySearch_Lvl1(array, target))

array = [5,6,7,8,9,10,1,2,3,4]
target = 3
print(BinarySearch_Lvl2(array, target))