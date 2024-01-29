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
}
