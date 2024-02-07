import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

        /* 
         * Guess My Number
         * 
         * Write a program that plays the game of "Guess My Number" with the user. The program should use a binary search algorithm to find the number. The user will think of a number between 1 and n. The program will make guesses and the user will tell the program to guess higher or lower. The program will continue to make guesses until the user tells the program that the guess is correct.
         */
       // int max = (Integer.parseInt(System.console().readLine("Enter n: ")) - 1);
       // int result4 = guessMyNumber(max);

        /*
         * Group Anagrams
         * 
         * Given an array of strings, group anagrams together.
         * 
         * Example 1:
         * Input: ["eat","tea","tan","ate","nat","bat"]
         * Output: [["ate","eat","tea"],["nat","tan"],["bat"]]
         */
        String[] A = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> result5 = groupAnagrams(A);
        System.out.println(result5);
    }


    // Week 1
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
    // Week 1
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

    // Week 2
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

    // Week 2 Lab
    // Guess My Number
    public static int guessMyNumber(int max) {
        int min = 0;
        // Check if the number is positive
        while (max < min) {
            max = (Integer.parseInt(System.console().readLine("Enter a positive integer for n: "))-1);
        }
        // Check if the number is in the array
        while (min <= max) {
            int middle = max + (min - max) / 2; //Returns rounded up
            System.out.print("Please think of a number between " + min + " and " + max + "."
                + "\nIs your number " + middle + "?"
                + "\nPlease enter C for correct, H for too high, or L for too low."
                + "\nEnter your response H/L/C: ");
            char response = System.console().readLine().charAt(0);
            // Check if the response is valid
            while (response != 'H' && response != 'L' && response != 'C') {
                System.out.print("Enter your response H/L/C: ");
                response = Character.toUpperCase(System.console().readLine().charAt(0));
            }
            // Check if the number is correct
            if (response == 'C') {
                System.out.println("Thank you for playing Guess My Number!");
                return middle;
            } else if (response == 'H') { // Check if the number is too high
                max = middle - 1;
            } else if (response == 'L') { // Check if the number is too low
                min = middle + 1;
            }
        } return -1; // Return -1 if the number is not in the array
    }

    // Week 3
    // Group Anagrams
    public static List<List<String>> groupAnagrams(String[] A) {
        Map<String, List<String>> map = new HashMap<>();
        for (String word : A) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            map.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(word);
        }
        return new ArrayList<>(map.values());
    }
}

