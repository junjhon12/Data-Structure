"""
An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay.
"""

def pay_conversion(hourly_wage, regular_hours, overtime_hours):
    overtime_pay = overtime_hours * (1.5 * hourly_wage)
    weekly_pay = hourly_wage * regular_hours + overtime_pay
    return print(f'Weekly Pay is {weekly_pay}')

print(pay_conversion(
    hourly_wage = float(input("Enter your pay hourly: ")),
    regular_hours = float(input("Enter hours of work: ")),
    overtime_hours = float(input("Enter hours of overtime: "))))