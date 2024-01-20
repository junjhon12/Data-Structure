import math

def guessMyNumber(max):
    min = 0 # the starting point of the range
    
    while max < min: # check if the range is valid
        max = int(input("Enter a positive integer for n: ")) - 1
    
    print('Welcome to Guess My Number!')
    
    while min <= max: 
        # find middle and return rounded up integer
        middle = math.ceil((min + max) / 2)
        print("Please think of a number between " + str(min) + " and " + str(max) + "."
              + "\nIs your number " + str(middle) + "?" 
              + "\nPlease enter C for correct, H for too high, or l for too low.")
        response = input('Enter your response H/L/C: ')[0].upper()
    
        while response != 'C' and response != 'L' and response != 'H': # check if the response is valid
            response = input('Enter your response H/L/C: ')[0].upper()
        
        if response == 'C': # check if the number is found
            print('Thank you for playing Guess My Number!')
            return middle
        elif response == 'H': # Check if the number is too high
            max = middle - 1
        elif response == 'L': # Check if the number is too low
            min = middle + 1
        
    return -1 # return -1 if the number is not found

max = int(input('Enter n: ')) - 1
result = guessMyNumber(max)