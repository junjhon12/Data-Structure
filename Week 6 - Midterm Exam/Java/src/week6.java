
/**
 * Midterm review
 * 
 * 1) Input : 19, 1, 15, 14, 79, 72, 61, 19
 * Use merge sort to sort the array
 * 
 * left = 19
 * right = 19
 * middle = 14
 * 
 * LSA = 19, 1, 15, 14
 * 19, 1    15, 14
 * 19 1     15 14
 * 1 | 19   14 | 15
 * compare then copy which is then move on
 * since 1 < 19, 1 is copied
 * since 14 < 15, 14 is copied
 *   1, 19  14, 15
 * 1, 14, 15, 19
 * 
 * LSA = 79, 72, 61, 19
 * 79, 72   61, 19
 * 79 72    61 19
 * 72 | 79  19 | 61
 * 
 * 72, 90   19, 61
 * 19, 61, 72, 79
 * 
 * 1, 14, 15, 19, 19, 61, 72, 79
 * 
 * Time complexity: O(Nlog_2N) where N is the length of the array.
 * 
 * array = {19, 1, 15, 14, 79, 72, 61, 19}
 * output = {1, 14, 15, 19, 19, 61, 72, 79}
 * 
 * n + n/2 + n/4 + n/8 + ... + 1 = 2n
 * 2n in terms of big O notation is O(n)
 */

 public class week6 {
    public static void main(String[] args) {
        int[] A = {19, 1, 15, 14, 79, 72, 61, 19};
        mergeSort(A, 0, A.length - 1);
        System.out.println("After sorting");
        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i] + " ");
        }

        
    }

    public static void mergeSort(int[] A, int low, int high) {
        if (low < high) {
            int middle = (low + high) / 2;
            mergeSort(A, low, middle);
            mergeSort(A, middle + 1, high);
            merge(A, low, middle, high);
        }
    }

    public static void merge(int[] A, int low, int middle, int high) {
        int[] helper = new int[A.length];
        for (int i = low; i <= high; i++) {
            helper[i] = A[i];
        }
        int i = low;
        int j = middle + 1;
        int k = low;
        while (i <= middle && j <= high) {
            if (helper[i] <= helper[j]) {
                A[k] = helper[i];
                i++;
            } else {
                A[k] = helper[j];
                j++;
            }
            k++;
        }
        while (i <= middle) {
            A[k] = helper[i];
            k++;
            i++;
        }
    }
 }