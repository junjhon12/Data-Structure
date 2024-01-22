import java.lang.Math;

public class lab2 {
    public static void main(String[] args) {
        int max = (Integer.parseInt(System.console().readLine("Enter n: ")) - 1);
        int result = guessMyNumber(max);
    }
    // guessMyNumber function
    public static int guessMyNumber(int max) {
        int min = 0;
        while (max < min) { // Checks if the number is positive
            max = (Integer.parseInt(System.console().readLine("Enter a positive integer for n: "))-1);
        }

        System.out.println("Welcome to Guess My Number!");
        // This loop will guess the number
        while (0 <= number) {
            System.out.println("Please think of a number between 0 and " + number + ".");
            System.out.println("Is your number " + Math.round(number / 2f) + "?");
            System.out.println("Please enter C for correct, H for too high, or L for too low.");
            System.out.print("Enter your response H/L/C: ");
            char response = new java.util.Scanner(System.in).next().charAt(0);
            // This loop will check if the response is valid
            while (response != 'C' && response != 'H' && response != 'L') {
                System.out.print("Enter your response H/L/C: ");
                response = Character.toUpperCase(System.console().readLine().charAt(0));
            }
            if (response == 'C') { // Checks if the number is correct
                System.out.println("Thank you for playing Guess My Number!");
                return middle;
            } else if (response == 'H') { // Checks if the number is too high
                max = middle - 1;
            } else if (response == 'L') { // Checks if the number is too low
                min = middle + 1;
            }
        }return -1; // Returns -1 if the number is not in the array
    } 
}
        