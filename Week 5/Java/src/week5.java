/**
         * Week 5 - 2/5/2024
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
         * memo = [1] x len(A) is the formula to create a memo array
         *                                                  A = [31, 32, 34, 33]                    
         * for i in range(len(A)-1, -1, -1):                
         *     for j in range(i+1, len(A)):                 
         *        if A[i] < A[j]:                            
         *           memo[i] = max(memo[i], memo[j] + 1)     
         *          
         * return max(memo)
         * 
         * Time Complexity: O(N^2) where N is the length of A. 
         * Space Complexity: O(N) where N is the length of A. The space complexity is in the memo array. O(len(A)) = O(N). Inside the mmeo array
         * 
         * Week 5 - 2/7/2024
         * 
         * Given: 10, 80, 30, 90, 40, 50, 70
         * 
         * [EXTREMELY IMPORTANT]
         * Quick Sort is a sorting algorithm that uses the divide and conquer strategy to sort an array.
         * It requires a pivot element to partition the array into two parts.
         * low (10) 80 30 90 40 50 (70) high <- pivot
         * i = low - 1, j = low
         * 
         * Chop it down to smaller pieces and sort them
         * 
         * Algorithm:
         * Partition for (j=low: j <= high-1; j++)       1) j= 10; <= 70 = 
         *     if (A[j] <= pivot)                        2) j= 80; 
         *        i++ or i = i+1                         3) j= 30; 
         *       swap (A[i] and A[j])                    4) j= 90; 
         * #For loop ends                                5) j= 40; 
         * swap A[i+1] and A[high]                       6) j= 50; 
         * return i+1
         * 
         * Time complexity: O(NlogN) where N is the length of A.        Space complexity: O(1)
         * 
         * The pivot is 70
         * 
         * [10, 80, 30, 90, 40, 50, 70] -> [10, 30, 40, 50, 70, 90, 80]
         * 
         * Meaning of partitioning: the pivot is in the right place
         * 
         * [10, 30, 40, 50, 70, 90, 80] 
         * pivot is now 80     
         * swap (A[i+1] and A[high])                      
         * return i++                                     
         * 
         * [10, 30, 40, 50, 70, 90, 80] -> [10, 30, 40, 50, 70, 80, 90]
         * 
         * Quick Sort = O(n) + O(n+log_2(n)) = O(nlog_2(n)) 
         * O(n) is the partitioning and O(nlog_2(n)) is the sorting
         * 
         * [10, 9, 7, 5, 4, 3, 2, 1]
         * Assign the last element as the pivot
         * n^2 is the worst case scenario
         * Reverse sorting is the worst case scenario
         */                                              

public class week5 {
    
    public static void main(String[] args) {
        
        int[] A = {31, 32, 34, 33};
        System.out.println(lengthOfLIS(A));
    }

    // Find the length of the longest increasing subsequence
    public static int lengthOfLIS(int[] A) {
        // Create a memo array
        int[] memo = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            memo[i] = 1;
        }
        // Loop through the array and find the longest increasing subsequence
        for (int i = A.length - 1; i >= 0; i--) {
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] < A[j]) {
                    // Find the maximum value of the memo array
                    memo[i] = Math.max(memo[i], memo[j] + 1);
                }
            }
        }
        int max = 0;
        // Find the maximum value of the memo array
        for (int i = 0; i < memo.length; i++) {
            max = Math.max(max, memo[i]);
        }
        return max;
    }

    public static void quickSort(int[] A, int low, int high) {
        if (low < high) {
            int pi = partition(A, low, high);
            quickSort(A, low, pi - 1);
            quickSort(A, pi + 1, high);
        }
    }
    
    public static int partition(int[] A, int low, int high) {
        int pivot = A[high];
        int i = low - 1;
        for (int j = low; j <= high - 1; j++) {
            if (A[j] <= pivot) {
                i++;
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        int temp = A[i + 1];
        A[i + 1] = A[high];
        A[high] = temp;
        return i + 1;
    }

}
