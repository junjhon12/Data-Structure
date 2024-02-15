def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    # Check if the array is valid
    while left<= right:
        mid = left + (right - left) // 2
        # If the target is in the middle
        if array[mid] == target:
            return f'{target} is in index {mid}'
        # If target is greater than search the right
        elif array[mid] < target:
            left = mid + 1
        # If target is lesser than search the left
        else:
            right = mid - 1
    
    return f'{target} is not inside the array'

array = [-10, -5, 0, 3, 7, 9, 12, 15]
target = 7
print(binarySearch(array, target))

array = [2, 4, 6, 8, 10]
target = 5
print(binarySearch(array, target))

def rotatedBinarySearch(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = left + (right - left) // 2
        # Checks if the target is at middle
        if array[middle] == target:
            return f'{target} is in index {middle}'
        elif array[left] <= array[middle]:  # Left half is sorted
            if array[left] <= target <= array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:  # Right half is sorted
            if array[middle] <= target <= array[right]:
                left = middle + 1
            else:
                right = middle - 1
    return f'{target} is not in the array'
        
array = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(rotatedBinarySearch(array, target))
array = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(rotatedBinarySearch(array,target))

def minElementBinarySerch(array):
    left = 0
    right = len(array) - 1
    # Checks if array is valid
    while left < right:
        middle = left + (right - left) // 2
        if array[middle] < array[right]:  # Right side is sorted
            right = middle
        else:  # Left side is sorted
            left = middle + 1
    return 'The minimum element is ' + str(array[left]) + '.'
    
array = [5,4,3,2,1]
print(minElementBinarySerch(array))
array = [6,7,8,9,4,5,3,2,1]
print(minElementBinarySerch(array))

# Need to study this
def gridBinarySearch(grid, target):
    rows = len(grid)
    cols = len(grid[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    while top <= bottom:
        mid_row = top + (bottom - top) // 2
        if target < grid[mid_row][0]:
            bottom = mid_row - 1
        elif target > grid[mid_row][-1]:
            top = mid_row + 1
        else:
            # Perform binary search within the selected row
            left = 0
            right = cols - 1
            while left <= right:
                mid_col = left + (right - left) // 2
                if target < grid[mid_row][mid_col]:
                    right = mid_col - 1
                elif target > grid[mid_row][mid_col]:
                    left = mid_col + 1
                else:
                    return 'Target is in row ' + str(mid_row) + ' and column ' + str(mid_col) + '.'
            return 'Target not found'
    return 'Target not found'
        
grid = [[3,     5,      10,     12],
        [13,    15,     20,     21],
        [22,    24,     26,     29],
        [30,    31,     35,     40]]
target = 26
print(gridBinarySearch(grid, target))
grid = [[3,     5,      10,     12],
        [13,    15,]]
target = 15
print(gridBinarySearch(grid, target))
"""
import math
def guessMyNumber(max):
    min = 0
    while max < min:
        max = int(input("Positive number: ")) - 1
    while min <= max:
        middle = math.ceil((min + max)/2)
        print("Between " + str(min) + " and " + str(max) +
              "\nIs your number " + str(middle) + " ?" + 
              "\nPlease enter C for correct, H for too high, or L for too low.")
        response = input('Enter response C/H/L: ')[0].upper()
        while response != 'C' and response != 'L' and response != 'H':
            response = input('Enter H/L/C: ')[0].upper()
        if response == 'C':
            print('Thanks for playing')
            return middle
        elif response == 'H':
            max = middle - 1
        elif response == 'L':
            min = middle + 1
    return -1
    
max = int(input('Enter n: ')) - 1
result = guessMyNumber(max)
"""

from collections import defaultdict
def groupAnagrams(array):
    sortedDictionary = defaultdict(list)
    for word in array:
        sortedWord = "".join(sorted(word))
        sortedDictionary[sortedWord].append(word)
    return list(sortedDictionary.values())
array = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(array))
array = ["listen", "silent", "program", "gram", "test", "tset"]
print(groupAnagrams(array))

def rearrangeArray(array, number):
    less = []
    equal = []
    greater = []
    
    for elements in array:
        if elements < array[number]:
            less.append(elements)
        elif elements == array[number]:
            equal.append(elements)
        else:
            greater.append(elements)
    return less + equal + greater

array = [3,5,2,6,8,4,4,6,4,4,3]
number = 5
print(rearrangeArray(array, number))