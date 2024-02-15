import java.util.HashMap;
/**
 * 1/29/2024 Week 4 - Recursion Introduction
 *  Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
 *  0 and 1 are the base cases, 0 is sometimes referred to as F(0) and 1 is F(1)
 *  F(2) = F(1) + F(0) = 1 + 0 = 1
 *  F(3) = F(2) + F(1) = 1 + 1 = 2
 *  F(4) = F(3) + F(2) = 2 + 1 = 3
 *  F(5) = F(4) + F(3) = 3 + 2 = 5
 *  F(6) = F(5) + F(4) = 5 + 3 = 8
 *  F(7) = F(6) + F(5) = 8 + 5 = 13
 *  F(8) = F(7) + F(6) = 13 + 8 = 21
 *  F(9) = F(8) + F(7) = 21 + 13 = 34
 *  Formula: F(n) = F(n-1) + F(n-2)
 * 
 * Tetris Steps 
 * If n = 3
 * 1) Take 1 step, 1 step, then 1 step = 3 steps
 * 2) Take 1 steps then 2 steps = 3 steps
 * 3) Take 2 steps then 1 step = 3 steps
 * 
 * If n = 5
 * 1) Take 1 step, 1 step, 1 step, 1 step, 1 step = 5 steps
 * 2) Take 1 step, 1 step, 1 step, 2 steps = 5 steps
 * 3) Take 1 step, 1 step, 2 steps, 1 step = 5 steps
 * 4) Take 1 step, 2 steps, 1 step, 1 step = 5 steps
 * 
 *                                     0
 *                                  /   \
 *                                1     2
 *                             /  \   /  \
 *                           2     3  3   4
 *                       /  \   / \   / \  / \
 *                     3   4  4  5  4  5 5  6
 *                 / \  / \ / \ / \ / \ / \ / \
 *              4  5 5 6 5 6 6 7 5 6 6 7 6 7 7 8
 *         / \ / \ / \ / \ / \ / \ / \ / \ / \
 *      5 6 6 7 6 7 7 8 6 7 7 8 7 8 8 9 6 7 7 8
 * 
 *  If n = 5, any number higher than 5 will fall off
 *  TIME COMPLEXITY: O(2^n)
 *  SPACE COMPLEXITY: O(n)
 */

public class week4 {
    public static void main(String[] args) {
        int n = 5;
        System.out.println(fibonacci(n));

        String message = "121";
        System.out.println(decode(message));

        /**
         * n = 5
         *                        F(5)
         *                     /        \
         *                F(4)          F(3)
         *             /     \        /     \
         *         F(3)     F(2)   F(2)    F(1)
         *       /    \   /    \  /   \
         *    F(2)  F(1) F(1) F(0) F(1) F(0)
         *  /   \
         * F(1) F(0)
         * 
         * TIME COMPLEXITY: O(2^n)
         * SPACE COMPLEXITY: O(n)
         */

        System.out.println(decode(message));
    }

    //Recursive Method - Fibonacci
    public static int fibonacci(int n) {
        if(n > 40) {
            throw new IllegalArgumentException("n is too large"
        + " to compute fibonacci");
        }
        else if (n == 0) {// Base case
            return 0;
        } else if (n <= 1) {
            return 1;
        } else {// Recursive case
            return fibonacci(n-1) + fibonacci(n-2);
        }

    }

    /*
     * Wednesdays 1/31/2024
     *   1
     *  n=5
     *     | 1
     *      n=4
     *         | 2                        1,1,2,3,5
     *          n=3                   f=0,1,1,2,3,5      The difference from Fibonacci is that the first two numbers are 1,1
     *            | 3
     *             n=2
     *               | 5
     *                n=1
     * -----------------|
     * 
     * Decoding Problem        String '121' - (121) 'ABA' : 1|2|1 \
     * A -> 1                               - (12|1) 'LA' : 12|1 ---> = 3 ways to decode
     * B -> 2                               - (1|21) 'AU' : 1|21  /               
     * C -> 3
     * D -> 4
     * E -> 5                  Leading 0 -> 0
     * F -> 6                  NOTE: Anything [GREATER THAN 26] is not a valid encoding
     * G -> 7
     * H -> 8
     * I -> 9
     * J -> 10                 '11106' -> KJF Allowed
     * K -> 11                 
     * L -> 12
     * M -> 13
     * N -> 14
     * O -> 15
     * P -> 16
     * Q -> 17
     * R -> 18
     * S -> 19
     * T -> 20
     * U -> 21
     * V -> 22
     * W -> 23
     * X -> 24
     * Y -> 25
     * Z -> 26
     * 
     * Example: '121'
     *                                             121
     *                                           /     \
     *                                          1       12
     *                                         / \     /  \          There are 3 ways to decode '121'
     *                                       2   21  1     X
     *                                      / \ /  \/ \   
     *                                     1   X   X    X
     */

    //Recursive Method - Decoding Problem for 1 step
    
   
        
        /**
         * Professor's Solution
         * def Decoding(self, S str) -> int:
         * D = {len(s) : 1} 
         * def decode(i)
         * if s[i] == '0':
         * return 0
         * if i in D:
         * return D[i]
         * n_ways = decode(i + 1)
         * if i + 1 < len(s) and s[i + 1] == '1' or (s[i + 1] == '2' and s[i + 2] in '0123456'):
         * n_ways += 1
         * D[i] = n_ways
         */

         

}
