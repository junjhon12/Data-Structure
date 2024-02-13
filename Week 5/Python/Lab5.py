def quick_sort(ARRAY):
    # Quick sort function
    low = 0
    high = len(ARRAY) - 1
    pivot = ARRAY[high]
    
    def partition(ARRAY, low, high):
        i = low - 1
        # Partition the array into two halves
        for j in range(low, high):
            # Left side is less than the pivot and the right side is greater than the pivot
            if ARRAY[j] < pivot:
                i += 1
                # Swap the elements
                ARRAY[i], ARRAY[j] = ARRAY[j], ARRAY[i]
        # Swap the pivot with the element at i + 1
        ARRAY[i + 1], ARRAY[high] = ARRAY[high], ARRAY[i + 1]
        return i + 1  
    
    # This function will help to sort the array from low to high
    def quick_sort_helper(ARRAY, low, high):
        if low < high:
            # Get the pivot index
            pi = partition(ARRAY, low, high)
            # Sort the left half
            quick_sort_helper(ARRAY, low, pi - 1)
            # Sort the right half
            quick_sort_helper(ARRAY, pi + 1, high)
            
    # Call the helper function
    quick_sort_helper(ARRAY, low, high)
    return ARRAY

ARRAY = []
print(quick_sort(ARRAY))

ARRAY = [1]
print(ARRAY)

ARRAY = [1, 1, 1, 1, 1, 1, 1]

ARRAY = [-7, -2, -3, -3, -1, -6]

ARRAY = [50, 11, 33, 21, 40, 50, 40, 40]
