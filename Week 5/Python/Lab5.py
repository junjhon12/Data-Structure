# Test Case 1 : NULL array
ARRAY = []
print(quick_sort(ARRAY)) # []

# Test Case 2 : Single element array
ARRAY = [1]
print(quick_sort(ARRAY)) # [1]

# Test Case 3 : Array with multiple copies of the same element
ARRAY = [1, 1, 1, 1, 1, 1, 1]
print(quick_sort(ARRAY)) # [1, 1, 1, 1, 1, 1, 1]

# Test Case 4 : Array with negative numbers
ARRAY = [-7, -2, -3, -3, -1, -6]
print(quick_sort(ARRAY)) # [-7, -6, -5, -4, -3, -2, -1]

ARRAY = [50, 11, 33, 21, 40, 50, 40, 40]
print(quick_sort(ARRAY)) 
# Expected Output : [11, 21, 33, 40, 50]

def quick_sort(ARRAY) {
    low = 0
    high = len(ARRAY) - 1
    pivot = ARRAY[high]
    def partition(ARRAY, low, high) {
        # i will start at the index before low
        i = low - 1
        for j in range(low, high) {
            if ARRAY[j] < pivot {
                i += 1
                ARRAY[i], ARRAY[j] = ARRAY[j], ARRAY[i]
                
                if ARRAY[j] == ARRAY[i] {
                    ARRAY.pop
                }
            }
        }
        
}