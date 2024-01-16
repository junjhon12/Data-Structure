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
        
        if target == middle:
            return f'Found Target: {target} at index {middle}'
        elif array[left] <= array[middle]:
            if target > array[middle] or target < array[left]:
                left = middle + 1
            else:
                right = middle - 1
        else:
            if target < array[middle] or target > array[right]:
                right = middle - 1
            else:
                left = middle + 1  

array = [1,2,3,4,5,6,7,8,9,10]
target = 5
print(BinarySearch_Lvl1(array, target))

array = [5,6,7,8,9,10,1,2,3,4]
target = 3
print(BinarySearch_Lvl2(array, target))