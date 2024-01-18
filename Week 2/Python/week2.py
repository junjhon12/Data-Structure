# Find the minimum element in a sorted and rotated array
# Solution
# left = 0
# right = len(array) - 1
# current_min = array[0]
# while left <= right:
#    if array[left] < array[right]:
#       current_min = min(current_min, array[left])
#       break
# With Binary Search
# middle = left + (right - left) // 2 (avoid overflow)
# current_min = min(current_min, array[mididle])
# if array[left] <= array[middle]:
# left = middle + 1 (search right side)
# else:
# right = middle - 1
# (out of while loop)
# return current_min
def BinarySearch_Lvl3(array):
    left = 0
    right = len(array) - 1
    current_min = array[0]
    
    while left <= right:
        middle = left + (right - left) // 2
        current_min = min(current_min, array[middle])
        if array[left] <= array[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return current_min
'''
def BinarySearch_Lvl3_2(array):
    left = 0
    right = len(array) - 1
    current_max = right
    
    while left <= right:
        middle = left + (right - left) // 2
        if array[right] >= array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return current_max
'''

# Simplistic solution
# loop within loop
# for loop through rows
# then for loop through columns
# if target == grid[row][column]:
# return True

# Binary Search Solution
# 1st binary search to find row
# 2nd binary search to find column
# 1st binary search

# topRow = 0
# bottomRow = len(grid) - 1
# while topRow <= bottomRow:
#   middleRow = top + (bottom - top) // 2
# if target > grid[middleRow][-1]:
#   topRow = middleRow + 1 (search bottom half)
# elif target < grid[middleRow][0]:
#   bottomRow = middleRow - 1 (search top half)
# else:
#   break
#
# 2nd binary search
# leftColumn = 0
# rightColumn = len(grid[0]) - 1
# while leftColumn <= rightColumn:
#   middleColumn = leftColumn + (rightColumn - leftColumn) // 2
# if target > grid[middleRow][middleColumn]:
#   leftColumn = middleColumn + 1 (search right half)
# elif target < grid[middleRow][middleColumn]:
#   rightColumn = middleColumn - 1 (search left half)
# else:
#   return True
def BinarySearch_Lvl4(grid, target):
    topRow = 0
    bottomRow = len(grid) - 1
    
    while topRow <= bottomRow:
        middleRow = topRow + (bottomRow - topRow) // 2

        if target > grid[middleRow][-1]:
            topRow = middleRow + 1
        elif target < grid[middleRow][0]:
            bottomRow = middleRow - 1
        else:
            break
        
    leftColumn = 0
    rightColumn = len(grid[0]) - 1
    
    while leftColumn <= rightColumn:
        middleColumn = leftColumn + (rightColumn - leftColumn) // 2
        
        if target == middleColumn:
            return f'Found Target: {target} at index {middleColumn}'
        elif grid[middleRow][leftColumn] <= grid[middleRow][middleColumn]:
            if target > grid[middleRow][middleColumn] or target < grid[middleRow][leftColumn]:
                leftColumn = middleColumn + 1
            else:
                rightColumn = middleColumn - 1
            
    
 
#Success
array = [5,6,7,8,9,10,0,2,3,4]
print(BinarySearch_Lvl3(array))

# Row is 3, 5, 10, 12
# Column is 3, 13, 22, 30
grid = [[3, 5, 10, 12],
        [13, 15, 20, 21],
        [22, 24, 26, 29],
        [30, 31, 35, 40]]
target = 26
print(BinarySearch_Lvl4(grid, target))
