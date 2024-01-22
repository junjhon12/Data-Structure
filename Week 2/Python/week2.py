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

# Using Binary Search to find minimum element in a sorted and rotated array
def BinarySearch_Lvl3(array):
    left = 0
    right = len(array) - 1
    current_min = array[0]
    while left <= right:# Checks if array is valid
        middle = left + (right - left) // 2# Gets middle index
        current_min = min(current_min, array[left])# Checks if left side is sorted
        if array[left] <= array[middle]: # left side is sorted
            left = middle + 1
        else: # right side is sorted
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

# Using Binary Search to find target in a 2D array
def BinarySearch_Lvl4(grid, target):
    topRow = 0
    bottomRow = len(grid) - 1
    
    while topRow <= bottomRow: # Checks if grid is valid
        middleRow = topRow + (bottomRow - topRow) // 2 # Gets middle index
        if target > grid[middleRow][-1]: # Checks if target is in bottom half
            topRow = middleRow + 1 # Searches bottom half
        elif target < grid[middleRow][0]: # Checks if target is in top half
            bottomRow = middleRow - 1 # Searches top half
        else: # Target is in middle row
            break
    
    leftColumn = 0 
    rightColumn = len(grid[0]) - 1 
    while leftColumn <= rightColumn: # Checks if row is valid
        middleColumn = leftColumn + (rightColumn - leftColumn) // 2
        if target > grid[middleRow][middleColumn]: # Checks if target is in right half
            leftColumn = middleColumn + 1 # Searches right half
        elif target < grid[middleRow][middleColumn]: # Checks if target is in left half
            rightColumn = middleColumn - 1 # Searches left half
        else: # Target is in middle column
            return 'Target is at row ' + str(middleRow) + ' and column ' + str(middleColumn) + '.' 
            
    
 
#Success
array = [5,6,7,8,9,1,2,3,4]
print(BinarySearch_Lvl3(array))

# Row is 3, 5, 10, 12
# Column is 3, 13, 22, 30
grid = [[3,     5,      10,     12],
        [13,    15,     20,     21],
        [22,    24,     26,     29],
        [30,    31,     35,     40]]
target = 15
print(BinarySearch_Lvl4(grid, target))
