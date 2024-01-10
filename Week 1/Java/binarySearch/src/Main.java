
public class Main {
    public static void main(String[] args) {
        int[] b = {1, 2, 3, 4, 5}; // The array
        int a = 3;// The number to search
        int result = binarySearch(b, a);// Using binary search
        System.out.println(result);// Print the result
    }

    // Binary search function
    public static int binarySearch(int[] b, int a) {
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
}
