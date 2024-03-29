A = [71, 72, 74, 73]

"""
1)First Test Case is always Null                            NULL
2)Second Test Case is if the array is empty                 []
3)Third Test Case is if the array has only one element      [7] -> longest increasing subsequence is [7]

The reason why it's called bottom-up is because we start from the bottom of the array and work our way up.

                                               []
[71]                       [72]                                 [74]                       [73]
[71,72][71,74][71,73]      [72,74][72,73]                       [74,73] 
[71,72,74][71,72,73]       [72,74,73]
[71,72,74,73]
    
    [71,72,74,73] is the longest increasing subsequence -> 4          
    

Week 5 2/7/2024 - Quick Sort
[10, 80, 30, 90, 40, 50, 70]

First, bound the array with a low and high index. The pivot is always the last element in the array.
Low = 10 High = 70 Pivot = 70

i = Low - 1

Partition the array into two halves. The left half is less than the pivot and the right half is greater than the pivot.
for (j = low; j <= high, j++) 
    if (array[j] < pivot)
        i++
        swap(array[i], array[j]) 
//End of the loop
swap(array[i + 1], array[high]) // Swap the pivot with the element at i + 1
return i + 1

Simulation:
[10, 80, 30, 90, 40, 50, 70] 
1) 10 < 70 = True => i = 0 => swap(10, 10) => [10, 80, 30, 90, 40, 50, 70]
2) 80 < 70 = False
3) 30 < 70 = True => i = 1 => swap(80, 30) => [10, 30, 80, 90, 40, 50, 70]
4) 90 < 70 = False
5) 40 < 70 = True => i = 2 => swap(80, 40) => [10, 30, 40, 90, 80, 50, 70]
6) 50 < 70 = True => i = 3 => swap(90, 50) => [10, 30, 40, 50, 80, 90, 70]
7) 70 < 70 = False
swap(80, 90) => [10, 30, 40, 50, 70, 90, 80]

[10, 30, 40, 50, 70, 90, 80] -> 70 is the pivot

Time Complexity: O(nlogn) -> Average Case

Worst case in time complexity is O(n^2) -> If the pivot is the smallest or largest element in the array

For any sorting algorithm, the best case is O(nlogn) and the worst case is O(n^2)
An example is if the array is reversed list. 
A = [10, 9, 7, 5, 3, 2, 1]

"""

def quickSort(array):
    low = 0
    high = len(array) - 1
    pivot = array[high]
    # Partition the array into two halves
    def partition(array, low, high):
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1 
    # This function purpose 
    def quickSortHelper(array, low, high):
        if low < high:
            # pi is the partitioning index
            pi = partition(array, low, high)
            quickSortHelper(array, low, pi - 1)
            quickSortHelper(array, pi + 1, high)
            
    quickSortHelper(array, low, high)
    return array

# Time Complexity of quickSort2 is O(nlogn) -> Average Case
def quickSort2(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort2(less) + [pivot] + quickSort2(greater)

print(quickSort([10, 80, 30, 90, 40, 50, 70])) # [10, 30, 40, 50, 70, 80, 90]
print(quickSort2([10, 9, 7, 5, 3, 2, 1])) # [1, 2, 3, 5, 7, 9, 10]

def quickSort(array):
    low = 0
    high = len(array) - 1
    # Partition the array into two halves
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        # The loop will iterate through the array and swap elements if the element is less than the pivot
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                # swap elements
                array[i], array[j] = array[j], array[i]
        # This will swap the pivot with the element at i + 1 because the pivot is the last element in the array
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
    # The pur
    def quickSortHelper(array, low, high):
        if low < high:
            # pi is the partitioning index
            pi = partition(array, low, high)
            quickSortHelper(array, low, pi - 1)
            quickSortHelper(array, pi + 1, high)
            
    quickSortHelper(array, low, high)
    return array

ARRAY = [50, 11, 33, 21, 40, 50, 40, 21, 40]
print(quickSort(ARRAY))