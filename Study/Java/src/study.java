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
    public static int binarySearchRotatedArray(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (array[mid] == target) {
                return mid;
            }
            if (array[left] <= array[mid]) { // If the left side is sorted
                if (target >= array[left] && target < array[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else { // If the right side is sorted
                if (target > array[mid] && target <= array[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1; // Add the missing return statement
    }
}

