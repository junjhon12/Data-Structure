
public class Main {
    public static void main(String[] args) {
        // The array
        int[] b = {1, 2, 3, 4, 5};
        // The number to search
        int a = 3;
        // Using binary search
        int result = binarySearch(b, a);
        // Print the result
        System.out.println(result);
    }

    // Binary search function
    public static int binarySearch(int[] b, int a) {
        // The array low and high
        int low = 0;
        int high = b.length - 1;
        // Checks if the array is empty or not
        while (low <= high) {
            // The middle of the array
            int mid = (low + high) / 2;
            // Checks if the number is in the middle
            if (a == b[mid]) {
                return mid;
                // Checks if the number is less than the middle
            } else if (a < b[mid]) {
                // Sets the high to the middle - 1
                high = mid - 1;
                // Checks if the number is greater than the middle
            } else if (a > b[mid]) {
                // Sets the low to the middle + 1
                low = mid + 1;
            }
        }
        // Returns -1 if the number is not in the array
        return -1;
    }
}
