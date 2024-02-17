"""
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
"""
#Updated version of binary search from leetcode
def binarySearch_V2(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return middle  # Return the index when target is found
    return f'Not Found'
            
array = [-10, -5, 0, 3, 7, 9, 12, 15]
target = 7
print(binarySearch_V2(array, target))
array = [2, 4, 6, 8, 10]
target = 5
print(binarySearch_V2(array, target))

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

def minElementBinarySearch(array):
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
print(minElementBinarySearch(array))
array = [6,7,8,9,4,5,3,2,1]
print(minElementBinarySearch(array))

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

def groupAnagrams(array):
    sortedDictionary = {}
    for word in array:
        sortedWord = "".join(sorted(word))
        # Check if sortedWord is already a key in the dictionary
        if sortedWord in sortedDictionary:
            # If yes, append the word to the list associated with the key
            sortedDictionary[sortedWord].append(word)
        else:
            # If not, create a new key-value pair with sortedWord as the key and a list containing word as the value
            sortedDictionary[sortedWord] = [word]
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
number = 4
print(rearrangeArray(array, number))

def rearrange_arrayP2(array,number):
    # low pointer
    low = 0
    for i in range(len(array)):
        if array[i] < number:
            array[low], array[i] = array[i], array[low]
            low += 1
    return array

array = [1, 3, 5, 7, 2, 4, 6, 8]
number = 5
print(rearrange_arrayP2(array,number))

def fibonacci(number):
    while number < 20:
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return (fibonacci(number-1) + fibonacci(number-2))
        
number = 15
print(fibonacci(number))

def climbStairs(number):
    while number < 20:
        if number == 0:
            return 1
        elif number == 1:
            return 1
        if number > 1:
            return climbStairs(number-1) + climbStairs(number-2)
        
number = 2
print(climbStairs(number))

def decoding(s: str) -> int:
    decodedDict = dict()
    
    def decode_count(i):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i in decodedDict:
            return decodedDict[i]
        result = decode_count(i+1)
        if i <= len(s) - 2 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
            s[i+1] == '1' or (s[i+1] == '2' and s[i+2] in '0123456')
            result += decode_count(i+2)
        decodedDict[i] = result
        return result
    return decode_count(0)
    
s = '121'
print(decoding(s))

import copy
def rotateMatrix(matrix):
    row = len(matrix)
    newMatrix = [[0 for i in range(row)] for j in range(row)]
    for i in range(row):
        for j in range(row):
            newMatrix[j][row - 1 - i] = matrix[i][j]
    for i in range(row):
        for j in range(row):
            matrix[i][j] = newMatrix[i][j]
    for row in matrix:
        print(row)
    return matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print('Rotated Matrix:')
rotatedMatrix = rotateMatrix(matrix)

def rotateInPlace(matrix):
    row = len(matrix)
    for i in range(row):
        for j in range(i, row):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(row):
        matrix[i] = matrix[i][::-1]
    for row in matrix:
        print(row)
    return matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print('Rotated Matrix in place:')
rotatedMatrixInPlace = rotateInPlace(matrix)

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

array = [10, 9, 7, 5, 3, 2, 1]
print(quickSort(array))