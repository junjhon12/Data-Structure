# Instructions:

#(1) (50 points)
#You are given an array of integers and an index x.
#Without sorting Re-arrange the array as below: elements less than array[x], followed by elements equal to array[x], followed by elements greater than array[x] 1
#Array, a = [3,5,2,6,8,4,4,6,4,4,3] and x = 5
#Write a Python Program that re-arranges the above given array exactly as shown below without using a sorting routine of any kind
#output array = [3,2,3,4,4,4,4,5,6,8,6]
#Here You are allowed to use an extra array to solve the problem.
#(2) (50 points)
#You are given an array of integers and an index x.
#Without sorting Re-arrange the array as below: elements less than array[x], followed by elements equal to array[x], followed by elements greater than array[x]
#Array, a = [3,5,2,6,8,4,4,6,4,4,3] and x = 5
#Write a Python Program that re-arranges the above given array exactly
#as shown below without using a sorting routine of any kind output array = [3,2,3,4,4,4,4,5,6,8,6]
#Here You are Not allowed to use an extra array to solve the problem.
#Hint : Keep three pointers to track boundaries. Low tracks elements less than a[x], Mid tracks elements equal to a[x], and High tracks elements
#greater a[x].Go through the array and place the numbers in the correct boundary.


#1
def rearrange_array(a, x):
    less = [] # stores elements less than the pivot
    equal = [] # stores elements equal to the pivot
    greater = [] # stores elements greater than the pivot
    for element in a:
        if element < a[x]: #if element is less than the pivot
            less.append(element)
        elif element == a[x]: #if element is equal to the pivot
            equal.append(element)
        else: #if element is greater than the pivot
            greater.append(element)
    return less + equal + greater

#2
def rearrange_arrayP2(a,x):
    # low, mid, high pointers
    low = 0 
    mid = 0 
    high = len(a)-1 
    
    while mid <= high:
        if a[mid] < x:  #if element is less than x
            a[low],a[mid] = a[mid],a[low] #swap elements
            low += 1 #low moves to the right
            mid += 1 #mid moves to the right
        elif a[mid] > x: #if element is greater than x
            a[high],a[mid] = a[mid],a[high] #swap elements
            high -= 1 #high moves to the left
        else: #if element is equal to x
            mid += 1 #mid moves to the right
    return a
   

a = [3,5,2,6,8,4,4,6,4,4,3]
x = 5
print(rearrange_array(a, x))
print(rearrange_arrayP2(a, x))

