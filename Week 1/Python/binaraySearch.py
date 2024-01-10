 # Bug: overflow due to the mid

def binary_search (a,b):
    low = 0 #First index
    high = len(b)-1 #Last index
    
    while low <= high: #Check if valid
        mid = (low + high) // 2 #Find the middle index
        if a == b[mid]: #If mid is the target
            return f'Target is found at index: {mid}' #Return mid if target is found in the middle
        elif a < b[mid]:#If target is smaller than mid
            high = mid - 1
        else:#If target is greater than mid
            low = mid + 1
    return f'Target is not found'# If target is not found

b = [3, 9, 10, 11, 15, 19]  # sorted array
a = 16  # target value
    
result = binary_search(a,b)
print(result)

b = []
a = 15  # target value
result2 = binary_search(a,b)
print(result2)

b = [15]
a = 15  # target value
result2 = binary_search(a,b)
print(result2)