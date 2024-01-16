 # Bug: overflow due to the mid

# Regular Binary Search
def binary_search_lvl1(a,b):
    low = 0 #First index
    high = len(b)-1 #Last index
    while low <= high: #Check if valid
        mid = low + (high-low)// 2 #Find the middle index
        if a == b[mid]: #If mid is the target
            return f'Target is found at index: {mid}' #Return mid if target is found in the middle
        elif a < b[mid]:#If target is smaller than mid
            high = mid - 1
        else:#If target is greater than mid
            low = mid + 1
    return 'Target is not found'# If target is not found

# Binaray Search with rotated array
def binary_search_lvl2(target, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif array[left] < array[mid]: # left side is sorted
            if target > array[mid] or target < array[left]: # search right side
                left = mid + 1 # search right side
            else:
                right = mid - 1 # search left side
        else: # right side is sorted
            if target < array[mid] or target > array[right]: # search left side
                right = mid - 1 # search left side
            else:
                left = mid + 1 # search right side
    return 'Not Found'


                



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
result = binary_search_lvl1(target,array)
print(result)

# Wendesday problem
# Find the minimum value, not the index but the value without using a linear search using binary search
array = [320, 10000, 3823, 9524, 1]
