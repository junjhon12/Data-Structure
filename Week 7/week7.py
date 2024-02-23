"""
Wednesday, 2/21/2024
How are arrays placed in memory?
    - Arrays are placed in memory in a contiguous manner. This means that the elements of the array are stored in a continuous block of memory. This allows for easy access to the elements of the array.
    
Representative size of an integer
    - The size of an integer is 4 bytes. This is because an integer is 32 bits and 32 bits is equal to 4 bytes.
The defacor standard for the size of an integer is 4 bytes. This is because the size of an integer is 32 bits and 32 bits is equal to 4 bytes.

int => 8 Bytes

How is it placed in memory?
    - An integer is placed in memory in a contiguous manner. This means that the integer is stored in a continuous block of memory. This allows for easy access to the integer. Contiguous memory is also known as sequential memory.

Why are arrrays so fast?
    - Arrays are so fast because they are placed in memory in a contiguous manner. This means that the elements of the array are stored in a continuous block of memory. This allows for easy access to the elements of the array. This allows for fast access to the elements of the array.
    
Base address of an array is the address of the first element of the array. This helps in accessing the elements of the array by using the base address and the index of the element.

Example: 10, 9, 2, 21, 32, 11, 5
int => 8 Bytes

A[0] = 10
A[4] = 32

How are the elements of an array accessed?
    - The elements of an array are accessed by using the base address of the array and the index of the element. The base address of an array is the address of the first element of the array. This helps in accessing the elements of the array by using the base address and the index of the element.
    
Base add + (type memory size * index)
Time complexity of accessing an element of an array is O(1) {constant time complexity.}
Example: 4000 + (8B * 4) = 4032
O(1) fastest time complexity

If A[9] it'll return an error because the array is only 7 elements long. 
Undefine behavior

Static array is an array that has a fixed size. The size of the array is determined at compile time. The size of the array cannot be changed at runtime.
Dynamic array is an array that has a variable size. The size of the array is determined at runtime. The size of the array can be changed at runtime.

How would you append if there is no more space in the array?
    - If there is no more space in the array, then you would create a new array with a larger size. You would then copy the elements of the old array into the new array. You would then add the new element to the new array. This is known as dynamic array resizing.
Can you byplace the dynamic array?
    - No, you cannot inplace the dynamic array. This is because the dynamic array is stored in a continuous block of memory. This means that the dynamic array cannot be inplace. This is because the dynamic array is stored in a continuous block of memory. This means that the dynamic array cannot be inplace.
    
Contiguous are non-negotiable in both static and dynamic arrays. This is because the elements of the array are stored in a continuous block of memory. This allows for easy access to the elements of the array.

Arrays are popular due to their constant time complexity for accessing elements. This is because the elements of the array are stored in a continuous block of memory. This allows for easy access to the elements of the array.

How can contiguous memory be broken down?
    - Contiguous memory can be broken down by using pointers
    
If we break the contigurous property, how would it look like?
    - If we break the contiguous property, then the elements of the array would not be stored in a continuous block of memory. This would make it difficult to access the elements of the array. This would make it difficult to access the elements of the array.
    
    [10, 9, 2, 21, 32, 11, 5]
    [10]
        [9]         
            [2]     [21]
                [32]
                    [11]
                    
Now how do we access the elements of the array?
    - The elements of the array are accessed by using the base address of the array and the index of the element. The base address of an array is the address of the first element of the array. This helps in accessing the elements of the array by using the base address and the index of the element.
    Elment 0 needs to know Element 1's address and so on. This is not efficient.
     CS word for address is [POINTER]
     
What are pointers?
    - Pointers are variables that store the memory address of another variable. This allows for easy access to the variable. This allows for easy access to the variable. Address location
    
If we want Element 0 to find Element 3, we use pointers. But doing so will sacrfice speed.
Linked Structure, CRUD operations are O(n) time complexity

How does a pointer knows the array has ended?
    - A pointer knows the array has ended when it reaches the end of the array. This is because the end of the array is marked by a special value known as the null terminator. The null terminator is a special value that marks the end of the array. This allows the pointer to know when the array has ended.
    
Linked Structure, CRUD operations are O(n) time complexity

Container as a class structure will give more freedom to the programmer.
"""