import java.util.Random;
public class study {
    
    public static void main(String[] args) {
        /*
         * Binary Search Practice problem from LeetCode
         * 
         * Given a sorted array of distinct integers and a target value, return the index if the target is found.
         * If not, return the index where it would be if it were inserted in order.
         * 
         * You must write an algorithm with O(log n) runtime complexity.
         * example 1:
         * Input: nums = [1,3,5,6], target = 5
         * Output: 2
         * 
         */
        int[] array = {1,3,5,6};
        int target = 5;
        int result = binarySearch(array, target);
        if (result == -1) {
            System.out.println("The number is not in the array");
        } else {
            System.out.println("The target is in the array " + result);
        }

        /*
         * Binary Search with rotated array Practice problem from LeetCode
         * 
         * There is an integer array nums sorted in ascending order (with distinct values).
         * Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
         * 
         * For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
         * 
         * Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
         */

        int[] array2 = {6, 7, 8, 9, 1, 2, 3, 4, 5};
        int target2 = 4;
        int result2 = binarySearchRotatedArray(array2, target2);
        if (result2 == -1) {
            System.out.println("The number is not in the array");
        } else {
            System.out.println("The target is in the array " + result2);
        }

        /*
         * Binary Search finding the minimum in both rotated and non-rotated array
         * 
         * There is an integer array nums sorted in ascending order (with distinct values).
         * Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
         * 
         * For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
         * 
         * Given the array nums after the rotation, return the minimum element of this array.
         * 
         * You must write an algorithm that runs in O(log n) time.
         * 
         * Example 1:
         * Input: nums = [3,4,5,1,2]
         * Output: 1
         * 
         * Example 2:
         * Input: nums = [4,5,6,7,0,1,2]
         * Output: 0
         */

        int[] array3 = {4, 5, 6, 7, 9, 11, 0, 1, 2};
        int result3 = binarySearchMinimum(array3);
        if (result3 == -1) {
            System.out.println("The number is not in the array");
        } else {
            System.out.println("The lowest number is " + result3);
        }



    }

    // Binary Search
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;
        // Check if array is empty
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (array[mid] == target) {
                return mid;
            } else if (array[mid] < target) { // if target is > mid
                left = mid + 1;
            } else if (array[mid] > target) { // if target is < mid, search left
                right = mid - 1;
            }
        }
        return -1; // if target is not in the array
    }

    // Binary Search with rotated array
    public static int binarySearchRotatedArray(int[] array, int target) {           // Array = [6, 7, 8, 9, 1, 2, 3, 4, 5] target = 4
        int left = 0;                                                               // left = 0, array[0] = 6
        int right = array.length - 1;                                               // right = 8, array[8] = 5

        while (left <= right) {                                                     // 0 <= 8 , remember it's checking the array length not the index
            int mid = left + (right - left) / 2;                                    // mid = 0 + (8 - 0) / 2 = 4, array[4] = 1
            if (array[mid] == target) {                                             // if 1 == 4, false
                return mid;                                                         // return 4, false
            }
            if (array[left] <= array[mid]) { // If the left side is sorted          // if 6 <= 1, false
                if (target >= array[left] && target < array[mid]) {                 
                    right = mid - 1;                                                
                } else {                                                                                    
                    left = mid + 1;                                                 
                }
            } else { // If the right side is sorted                                 // if 6 > 1, true
                if (target > array[mid] && target <= array[right]) {                // if 4 > 1 && 4 <= 5, true
                    left = mid + 1;                                                 // left = 4 + 1 = 5  = [2, 3, 4, 5]
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1; // Add the missing return statement
    }

    // Binary Search finding the minimum in both rotated and non-rotated array
    public static int binarySearchMinimum(int[] array) {                            // Array = [4, 5, 6, 7, 9, 11, 0, 1, 2]
        int left = 0;                                                               // left = 0                        
        int right = array.length - 1;                                               // right = 8
        // Check if array is empty
        while (left < right) {
            int mid = left + (right - left) / 2;                                    // mid = 0 + (8 - 0) / 2 = 4, array[4] = 9      // mid = 5 + (8 - 5) / 2 = 6, array[6] = 0
            if (array[mid] < array[right]) {                                        // if 9 < 2, false                              // if 0 < 2, true
                right = mid;
            } else {                                                                // if 9 > 2, true
                left = mid + 1;                                                     // left = 4 + 1 = 5
            }
        }
        return array[left];
    }

    // Binary Search with 2D array
}

