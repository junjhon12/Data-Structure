
public class lab2 {
    public static void main(String[] args) {
        System.out.print("Enter n: ");
        int number = new java.util.Scanner(System.in).nextInt() - 1;

        guessMyNumber(number);
    }
    // This method will guess the number
    public static int guessMyNumber(int number) {
        
        while (number < 0) { // Checks if the number is positive
            System.out.print("Enter a positive integer for n: ");
            number = new java.util.Scanner(System.in).nextInt() - 1;
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
                response = new java.util.Scanner(System.in).next().charAt(0);
            }
            // This loop will check if the response is correct
            if (response == 'C') {
                System.out.println("Thank you for playing Guess My Number!");
                break;
            } else if (response == 'H') {
                // If too high, the number will be divided by 2
                number = Math.round(number / 2);
            } else if (response == 'L') {
                // If too low, the number will be multiplied by 1.5 to round up
                number = Math.round(number * 1.5f);
            }
            
        }return number;
    } 
}
        