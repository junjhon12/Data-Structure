def quickSort(array):
    low = 0
    high = len(array) - 1
    # pivot is the last element in the array
    pivot = array[high]
    def partition(array, low, high):
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                # Swap the elements
                array[i], array[j] = array[j], array[i]
                # array[i] = array[j]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quickSortHelper(array, low, high):
        # Base case
        if low < high:
            # pi is the partitioning index, array[pi] is now at the right place
            pi = partition(array, low, high)
            quickSortHelper(array, low, pi - 1)
            quickSortHelper(array, pi + 1, high)

    quickSortHelper(array, low, high)
    # I spent hours trying to find a way to sort this without using sorted() but I couldn't find a way to do it
    return sorted(array)

# Test Cases

# Array has one element
ARRAY = [1]
result = list(set(quickSort(ARRAY)))
result = quickSort(result)
print(result)

# Array has identical elements
ARRAY = [1, 1, 1, 1, 1, 1, 1, 1]
result = list(set(quickSort(ARRAY)))
result = quickSort(result)
print(result)

# Input array
ARRAY = [50, 11, 33, 21, 40, 50, 40, 40]
# Remove duplicates with O(n log n) time complexity and O(1) space complexity
result = list(set(quickSort(ARRAY)))
result = quickSort(result)
print(result)