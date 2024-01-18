public class week2 {
    
    public static void main(String[] args) {
        /** 
        int[] array = {4, 5, 6, 7, 9, 11, 0, 1, 2};
        int result = binary_search_Lvl3(array);
        if (result == -1) { // Checks if the number is in the array
            System.out.println("The number is not in the array"); 
        } else {
            System.out.println("The lowest number is " + result);
        }*/

        int[][] grid = {
            {8, 9, 10, 11},
            {13, 14, 15, 16},
            {17, 18, 19, 20},
            {25, 30, 32, 35}
        };
        int target = 19;
        int result2 = binary_Search_Lvl4(grid, target);
        if (result2 == -1) { // Checks if the number is in the array
            System.out.println("The number is not in the array"); 
        } else {
            System.out.println("The target is in the array " + result2);
        }
    }
   
    //Wednesday - Finding the minimum in a roatated array
    // int[] array = {4, 5, 6, 7, 9, 11, 0, 1, 2}
    // Bound to return the minimum element in the array (0)
    //public static int binary_Search_Lvl3(int[] array) {

    //}

    
    // Finding target in a grid
    // [8   9   10  11]
    // [13  14  15  16]
    // [17  18  19  20]
    // [25  30  32  35]
    // target = 19

    // Solution:
    // 1. Find the row that's not lower or higher than the target
    // 2. Fin the column that's not lower or higher than the target
    // 3. Return the target if it's found, otherwise return -1

    public static int binary_Search_Lvl4(int[][] grid, int target) {
        int top = 0;
        int bottom = grid.length - 1;

        while (top <= bottom) {
            int middle_row = top + (bottom - top) / 2;

            if (target == grid[middle_row][0])
                return grid[middle_row][0];
            else if (target > grid[middle_row][-1]) {
                top = middle_row + 1;
            } else if (target < grid[middle_row][0]) {
                bottom = middle_row - 1;
            }
        } return -1;
    }
}

