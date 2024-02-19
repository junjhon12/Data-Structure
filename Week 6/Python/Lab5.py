def mergeSort(array):
    while len(array) > 1:
        middle = len(array) // 2
        left = mergeSort(array[:middle])
        right = mergeSort(array[middle:])
        return merge(left, right)
    
def merge(left, right):
    mergedArray = []
    leftCount = 0
    rightCount = 0
    while len(left) > leftCount and len(right) > rightCount:
        if left[leftCount] < right[rightCount]:
            mergedArray.append(left[leftCount])
            leftCount += 1
        elif left[leftCount] > right[rightCount]:
            mergedArray.append(right[rightCount])
            rightCount += 1
        else:
            mergedArray.append(left[leftCount])
            leftCount += 1
            rightCount += 1
            
    mergedArray.extend(left[leftCount])
    mergedArray.extend(right[rightCount])
    return mergedArray

def sorted(array):
    sortedArray = []
    number = None
    for i in array:
        if i != number:
            sortedArray.append(i)
            number = i
    return sortedArray

def sortedArray(array):
    sortedArrayOne = mergeSort(array)
    sortedArrayTwo = sorted(sortedArrayOne)
    return sortedArrayTwo
    
    
array =  [50, 11, 33, 21, 40, 50, 40, 21, 40]
print(mergeSort(array))