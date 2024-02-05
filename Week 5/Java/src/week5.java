/**
         * Week 5 2/5/2024
         *  
         * UNIT TEST TAKING is highly recommended since it is a good way to test your code and make sure it works as expected.
         * Unit test taking is a process of testing individual units or components of a software.
         * 
         * Problem 1 : Array A = [31, 32, 34, 33]
         * We got to return the length of the longest, strictly, increasing subsequesnce.
         * 
         * A = [ 31 , 32 , 34 , 33 ]        Subsequence e.g -> [34, 33] subsequences need not be contiguous
         *       00   01   02   03          Contiguous means that the elements are adjacent to each other
         * 
         *  [34, 33] is not an increasing subsequence, therefore, the longest increasing subsequence is [31, 32, 34]
         * Example of a subsequence that is increasing but not necessarily contiguous is [31, 34]
         * Example of a subsequence that is contiguous and increasing is [31, 32, 34] also strictly increasing
         * 
         * Test Cases: 
         *      A = [] -> NULL longest increasing subsequence is 0
         *      B = [71] -> 1 Base case longest increasing subsequence is 1, length is 1
         *      C = [19, 19, 19, 19] -> 1 longest increasing subsequence is 1, length is 1. [C IS NO DIFFERENT FROM B]
         * 
         *      D = [31, 32, 33] -> 3 longest increasing subsequence is 3, length is 3.
         *      E = [31, 32, 34] -> Is contiguous and length is 3
         *      
         * Contigious is not a faactor, starting at 0 is not a factor, the only factor is the length of the longest increasing subsequence
         * 
         *                                                   Before Starting
         *                 [31]                          [32]                            [34]                            [33]
         *             [31,32][31,34][31,33]          [32,34][32,33]                [34,33]
         *         [31,32,34][31,32,33] Out of bounds [32,34,33] 
         *    [31,32,34,33]  Out of bounds          
         * This is NOT valid since it's not strictly increasing
         * 
         * Memoization is a technique used to store the results of expensive function calls and return the cached result when the same inputs occur again.
         * 
         * memo = [1] x len(A)
         *                                                  A = [31, 32, 34, 33]                    
         * for i in range(len(A)-1, -1, -1):                33 -> 34 -> 32 -> 31                   1) 33
         *     for j in range(i+1, len(A)):                 34 -> 33 -> 32 -> 31                      34
         *        if A[i] < A[j]:                           if 33 < 34: 33 < 33: 33 < 32: 33 < 31     33 < 32 False    
         *           memo[i] = max(memo[i], memo[j] + 1)    memo[3] = max(1, 1 + 1) = 2               
         *  
         * return max(memo)
         * 
         * Time Complexity: O(N^2) where N is the length of A. 
         * Space Complexity: O(N) where N is the length of A. The space complexity is in the memo array. O(len(A)) = O(N)
         */

public class week5 {
    
    public static void main(String[] args) {
        
        int[] A = {31, 32, 34, 33};
        System.out.println(lengthOfLIS(A));

    }

    // Find the length of the longest increasing subsequence
    public static int lengthOfLIS(int[] A) {
        int[] memo = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            memo[i] = 1;
        }
        for (int i = A.length - 1; i >= 0; i--) {
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] < A[j]) {
                    memo[i] = Math.max(memo[i], memo[j] + 1);
                }
            }
        }
        int max = 0;
        for (int i = 0; i < memo.length; i++) {
            max = Math.max(max, memo[i]);
        }
        return max;
    }
}
