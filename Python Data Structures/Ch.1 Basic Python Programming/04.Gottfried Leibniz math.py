"""
The German mathematician Gottfried Leibniz developed the following method
to approximate the value of π:
π/4 = 1 - 1/3 + 1/5 - 1/7 + …
Write a program that allows the user to specify the number of iterations used in
this approximation and displays the resulting value.
"""
def Gottfried_Leibniz_Approx(iterations):
    pi = 0
    for i in range(iterations):
        pi += ( (i / (2 * i + 1)))
        if i % 2 == 0:
            pi += 1 / (2 * i + 1)
        else:
            pi -= 1 / (2 * i + 1)
        
    return f'The pi is {pi}'

print(Gottfried_Leibniz_Approx(int(input("Enter number n: "))))