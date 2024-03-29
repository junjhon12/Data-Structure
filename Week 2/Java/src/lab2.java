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
        System.out.println("Welcome to Guess My Number!"); // Introduction after the number is positive
        while (min <= max) { // Checks if the number is in the array
            int middle = max + (min - max) / 2; //Returns rounded up
            System.out.print("Please think of a number between " + min + " and " + max + "."
                + "\nIs your number " + middle + "?"
                + "\nPlease enter C for correct, H for too high, or L for too low."
                + "\nEnter your response H/L/C: ");
            char response = System.console().readLine().charAt(0);
            while (response != 'H' && response != 'L' && response != 'C') { // Checks if the response is valid
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