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

# Binaray Search with 
def binary_search_lvl2(a, b):
    low = 0
    high = len(b) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a == b[mid]:
            return 'Target is found at index: {}'.format(mid)
        elif b[low] <= b[mid]:
            if a >= b[mid] or a < b[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if a <= b[mid] or a > b[high]:
                high = mid - 1
            else:
                low = mid + 1
    return 'Target is not found'

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

b = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
a = 5
result = binary_search_lvl2(a,b)
print(result)