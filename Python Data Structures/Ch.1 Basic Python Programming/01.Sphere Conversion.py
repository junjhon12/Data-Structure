"""
Write a program that takes the radius of a sphere (a floating-point number) as
input and outputs the sphere’s diameter, circumference, surface area, and volume.
"""

def sphere_conversion(radius):
    diameter = 2 * radius
    circumference = 2 * 3.14159 * radius
    surface_area = 4 * 3.14159 * radius ** 2
    volume = 4 / 3 * 3.14159 * radius ** 3
    return print(f"Diameter: {diameter}\nCircumference: {circumference}\nSurface Area: {surface_area}\nVolume: {volume}")

print(sphere_conversion(radius = float(input("Enter the radius of the sphere: ")) ))