public class week1 {
    public static void main(String[] args) {
        
        //Monday - Binary search Level 1
        int[] array = {1,2,3,4,5,6,7,8,9,0}; // The array
        int target = 5; // The number to search

        // Using binary search level 1
        int result = binary_Search_Lvl1(array, target);
        if (result == -1) { // Checks if the number is in the array
            System.out.println("The number is not in the array"); 
        } else {
            System.out.println("The target is in the array " + result);
        }

        //Tuesday - Binary search Level 2 - Rotated array
        int[] array2 = {6, 7, 8, 9, 1, 2, 3, 4, 5}; // The array
        int target2 = 5; // The number to search
        int result2 = binary_Search_Lvl2(array2, target2); // Using binary search level 2
        if (result2 == -1) { // Checks if the number is in the array
            System.out.println("The number is not in the array");
        } else {
            System.out.println("The target is in the array " + result2);
        }
    }
    // --------------------------------------------------------------------------------------------------------------

    // Monday - Binary search Level 1
    // int[] array = {1,2,3,4,5,6,7,8,9};
    // int target = 5;
    public static int binary_Search_Lvl1(int[] array, int target) {
        int leftIndex = 0; // leftIndex element will be 1
        int rightIndex = array.length - 1; // rightIndex element will be 9

        while (leftIndex <= rightIndex) { // while 1 <= 9
            int middleIndex = leftIndex + (rightIndex - leftIndex) / 2; // middleIndex element will be 5

            if (target == array[middleIndex]) { // if target == 5, return middleIndex
                return middleIndex;
                // searching on the left side
            } else if (target < array[middleIndex]) { // if target < 5, rightIndex will be 4, searching between [1,2,3,4]
                rightIndex = middleIndex - 1;
                // searching on the right side
            } else if (target > array[middleIndex]) { // if target > 5, leftIndex will be 6, searching between [6,7,8,9]
                leftIndex = middleIndex + 1;
            }
        }
        return -1;
    }

    // Tuesday - Binary search Level 2 - Rotated array
    // int[] array = {6, 7, 8, 9, 0, 1, 2, 3, 4, 5};
    // int target = 4;
    public static int binary_Search_Lvl2(int[] array, int target) {
        int leftIndex = 0; // leftIndex element will be 6
        int rightIndex = array.length - 1; // rightIndex element will be 5

        while (leftIndex <= rightIndex) {
            int middleIndex = leftIndex + (rightIndex - leftIndex) / 2; // middleIndex element will be 0
            if (target == array[middleIndex]) { // if target == 0, 4 == 0 NO
                return middleIndex;
                // searching on the left side
            } else if (array[leftIndex] < array[middleIndex]) { // if 6 <= 0, 6 <= 0 NO
                if (target > array[middleIndex] || target < array[leftIndex]) { // if target >= 0 or target < 6
                    leftIndex = middleIndex + 1; // leftIndex will be 1, searching between [7,8,9,0]
                } else {
                    rightIndex = middleIndex - 1; // rightIndex will be 3, searching between [6,7,8,9]
                }
                // searching on the right side
            } else { // if 6 > 0, 6 > 0 YES
                if (target < array[middleIndex] || target > array[rightIndex]) { // if target < 2 or target > 5, 4 < 2 or 4 > 5 NO
                    rightIndex = middleIndex - 1; // rightIndex will be 1
                } else { // if target > 2 or target < 5, 4 > 2 or 4 < 5 YES
                    leftIndex = middleIndex + 1; // leftIndex will be 3, searching between [3,4,5], 4 == 4 YES
                }
            }
        }
        return -1;

        //Simulation of the binary search level 2
        // Array : [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
        // Target: 4
        // int leftIndex = 0; so 6
        // int rightIndex = 9; so 5
        // int middleIndex = 0 + (9 - 0) / 2 = 4; so 0
        // if (4 == 0) NO
        // else if (6 <= 0) NO
        // else if (6 > 0) YES
        //   if (4 < 0 || 4 > 5) NO
        //   else (4 > 2 || 4 < 5) YES
        //    leftIndex = 3; so 3 [3,4,5]
        // int middleIndex = 3 + (5 - 3) / 2 = 4; so 4

        
        
    }
}