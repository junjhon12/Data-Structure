def problem6(last_name, hourly_wage, hour_worked):
    wage = hourly_wage * hour_worked
    print("{:<15} {:<15} {:<15}".format("Last Name", "Hourly Wage", "Wage Earned"))
    answer = ''
    while answer != 'q':
        print("{:<15} {:<15} {:<15}".format(last_name, hourly_wage, wage))
        answer("Add another employee? y/n ")
        if answer != 'q':
            print(problem6(last_name = input("New last name: ")))
            print(problem6(hourly_wage = float(input("New hourly wage: "))))
            print(problem6(hour_worked = float(input("New hours worked: "))))
        else:
            answer = 'q'
    return print("{:<15} {:<15} {:<15}".format(last_name, hourly_wage, wage))

print(problem6("le", 5, 10))        
