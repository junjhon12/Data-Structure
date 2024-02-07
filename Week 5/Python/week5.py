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
"""