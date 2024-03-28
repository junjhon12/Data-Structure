"""
A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet
high, the index is 0.6 and the total distance traveled by the ball is 16 feet after one
bounce. If the ball were to continue bouncing, the distance after two bounces
would be 10 ft 1 6 ft 1 6 ft 1 3.6 ft 5 25.6 ft. Note that distance traveled for
each successive bounce is the distance to the floor plus 0.6 of that distance as the
ball comes back up. Write a program that lets the user enter the initial height
of the ball and the number of times the ball is allowed to continue bouncing.
Output should be the total distance traveled by the ball.
"""

def bounce_conversion(height, bounce):
    distance = 0
    bounce_height = height - 4
    for bounces in range(0, bounce - 1):
        distance += bounce_height + (bounce * bounce_height)
        bounce_height *= (bounce_height / height)
        return f'Total distance traveled is {distance}'
    
print(bounce_conversion(
    height = int(input("Enter height: ")),
    bounce = int(input("Enter number of bounces: "))
))