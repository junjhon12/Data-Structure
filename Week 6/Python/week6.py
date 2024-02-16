A = [50, 11, 33, 21, 40, 50, 40, 40, 21]
j,low = 0,0
i = low - 1
high = len(A)-1 #pivot is last element
'''
partition for (j=low; j <= high-1, j++) #j incrememnt by 1
    if A[j] < pivot:
        i = i + 1 #increment, i at 10
        swap(A[i], A[j]) 
    }

}//for loop ends 
swap(A[i+1],A[high])
return i + 1

'''
#output: [10,30,40,50,70,90,80]#pivot is 70, where left is sorted and right isn't. run recursively on right/left
#pivot is always in correct index position
#half a runtime (recursion) is log2(n), overall: O(n*log2(n)) [+ o(n)]. average case.
#where O(n) is linear time median. worst case is o(nlog(n) #only if pivot is median

A_prime = [10,9,7,5,3,2,1] #input, quicksort. use code above. 
#pivot is 1. 
#worst case is O(n^2) ; running partition n times: nxn