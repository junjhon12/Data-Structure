import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class assignment1 {
    public static void main(String[] args) {
        // Test cases
        
        // Test case Null
        int[] null1 = {};
        int[] null2 = {};
        List<Integer> result = intersectionLvl1(null1, null2);
        System.out.println(result);
        result = intersectionLvl2(null1, null2);
        System.out.println(result);
        result = intersectionLvl3(null1, null2);
        System.out.println(result);

        // Test case identical arrays
        int[] identical1 = {1, 2, 3, 4, 5};
        int[] identical2 = {1, 2, 3, 4, 5};
        result = intersectionLvl1(identical1, identical2);
        System.out.println(result);
        result = intersectionLvl2(identical1, identical2);
        System.out.println(result);
        result = intersectionLvl3(identical1, identical2);
        System.out.println(result);

        // Test case different array lengths
        int[] diffLength1 = {1, 2, 3, 4, 5};
        int[] diffLength2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        result = intersectionLvl1(diffLength1, diffLength2);
        System.out.println(result);
        result = intersectionLvl2(diffLength1, diffLength2);
        System.out.println(result);
        result = intersectionLvl3(diffLength1, diffLength2);
        System.out.println(result);

        // Original test case
        int[] array1 = {1, 6, 9, 10, 11, 21};
        int[] array2 = {2, 6, 9, 11, 17, 21};
        result = intersectionLvl1(array1, array2);
        System.out.println(result);
        result = intersectionLvl2(array1, array2);
        System.out.println(result);
        result = intersectionLvl3(array1, array2);
        System.out.println(result);
    }

    // Find the intersection of two sorted arrays
    // Time complexity is O(m * n)
    public static List<Integer> intersectionLvl1(int[] array1, int[] array2) {
        List<Integer> result = new ArrayList<>();
        int i = 0; // Pointer for array1
        int j = 0; // Pointer for array2

            // Check if the pointers are within the bounds of the arrays
            while (i < array1.length && j < array2.length) {
                // If the elements are equal, add it to the result list
                if (array1[i] == array2[j]) {
                    result.add(array1[i]);
                    i++;
                    j++;
                // If the element in array1 is smaller, advance its pointer    
                } else if (array1[i] < array2[j]) {
                    i++;
                // If the element in array2 is smaller, advance its pointer    
                } else {
                    j++;
                }
            }
            return result;
        }

    // Time complexity is O(m * log(n))
    public static List<Integer> intersectionLvl2(int[] arr1, int[] arr2) {
        // Create a list to store the result
        List<Integer> result = new ArrayList<>();
        // If the first array is shorter, swap the arrays
        if (arr1.length < arr2.length) {
            int[] temp = arr1;
            arr1 = arr2;
            arr2 = temp;
        }
        Arrays.sort(arr2); // Sorting the shorter array for binary search
        for (int num : arr1) {
            // If the number is in the second array and not in the result list, add it to the result list
            if (Arrays.binarySearch(arr2, num) >= 0 && !result.contains(num)) {
                result.add(num);
            }
        }
        return result;
    }

    // Time complexity is O(m + n)
    public static List<Integer> intersectionLvl3(int[] arr1, int[] arr2) {
        // Create a list to store the result
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        // Loop through the arrays and find the intersection
        while (i < arr1.length && j < arr2.length) {
            // If the elements are equal, add it to the result list
            if (arr1[i] == arr2[j]) {
                // If the result list is empty or the last element is not equal to the current element, add it to the result list
                if (result.isEmpty() || arr1[i] != result.get(result.size() - 1)) {
                    result.add(arr1[i]);
                }
                i++;
                j++;
                // If the elements are not equal, move the pointer of the smaller element
            } else if (arr1[i] < arr2[j]) {
                i++;
                // If the elements are not equal, move the pointer of the smaller element
            } else {
                j++;
            }
        }
        return result;
    }
}
