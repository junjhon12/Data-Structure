 # Bug: overflow due to the mid

# Regular Binary Search
def binary_search_lvl2(target, array):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target == array[mid]:
            return mid
        elif array[l] < array[mid]: # left side is sorted
            if target > array[mid] or target < array[l]: # search right side
                l = mid + 1 # search right side
            else:
                r = mid - 1 # search left side
        else: # right side is sorted
            if target < array[mid] or target > array[r]: # search left side
                r = mid - 1 # search left side
            else:
                l = mid + 1 # search right side
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
target = 11
result = binary_search_lvl2(target,array)
print(result)

