
public class Main {
    public static void main(String[] args) {
        /*  
        // Monday
        int[] b = {1, 2, 3, 4, 5}; // The array
        int a = 1;// The number to search
        int result = binarySearch(b, a);// Using binary search
        if (result == -1) {// Checks if the number is in the array
            System.out.println("The number is not in the array");// Print the result
        } else {
            System.out.println("The number is in the array");// Print the result
        }*/

        // Tuesday - Binary search where the array is rotated or not sorted
        int[] c = {4, 5, 6, 7, 9, 0, 1, 2};
        int a = 5;
        int result = binarySearch_Lvl2(c, a);
        if (result == -1) {
            System.out.println("The number is not in the array");
        } else {
            System.out.println("The number is in the array " + result);
        }

        
    }   

    
    //Monday
    // Binary search function
    public static int binarySearch_Lvl1(int[] b, int a) {
        int low = 0;// The array low and high
        int high = b.length - 1;
        while (low <= high) {// Checks if the array is empty or not
            int mid = (low + high) / 2;// The middle of the array           
            if (a == b[mid]) { // Checks if the number is in the middle
                return mid;            
            } else if (a < b[mid]) { // Checks if the number is less than the middle              
                high = mid - 1;// Sets the high to the middle - 1             
            } else if (a > b[mid]) {// Checks if the number is greater than the middle           
                low = mid + 1; // Sets the low to the middle + 1
            }
        }
        // Returns -1 if the number is not in the array
        return -1;
    }

    //Tuesday
    // Binary search function where the array is rotated/ot sorted
    public static int binarySearch_Lvl2(int[] c, int a) {
        int low = 0; // The array low and high
        int high = c.length - 1;
        while (low <= high) { // Checks if the array is empty or not
            int mid = low + (high - low) / 2; // The middle of the array
            if (a == c[mid]) { // Checks if the number is in the middle
                return mid; 
            }else if (c[low] <= c[mid]) { // Checks if the array is sorted
                if (a >= c[mid] || a < c[low]) { // Checks if the number is in the middle, number is greater than the middle, or number is less than the low
                    low = mid + 1; // Sets the low to the right of the middle
                }else {  
                    high = mid - 1; // Sets the high to the left of the middle
                }
        }   else {
                if (a < c[mid] || a > c[high]) { // Checks if the number is in the middle, number is less than the middle, or number is greater than the high
                    high = mid - 1; // Sets the high to the left of the middle
                }else {
                    low = mid + 1; // Sets the low to the right of the middle
                }
            }
        }  
        return -1;
    }

     

}
