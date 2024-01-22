import math
def geussMyNumber(number):
    lowest = 0
    highest = number
    while (lowest > highest):
        print(f'Enter a positive integer for n: ')
        number = int(input())        
        return number
    print('Welcome to Guess My Number!')
    
    while (lowest < highest):
        middle = (lowest + highest) // 2
        print('Please think of a number between 0 and ' + str(number) + '!')
        print('Is your number ' + str(number // 2) + '?')
        print('Please enter C for correct, H for too high, and L for too low: ')
        print('Enter your response H/L/C: ')
        response = input()
        
        if (response == 'H'):
            number = number // 2
        elif (response == 'L'):
            number = math.ceil(number * 1.5)
        elif (response == 'C'):
            print('Thank you for playing Guess My Number!')
            break   
        
print('Enter n: ')
number = int(input())
geussMyNumber(number)