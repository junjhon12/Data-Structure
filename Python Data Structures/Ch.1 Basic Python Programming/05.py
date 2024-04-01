def problem5(purchase_price):
    down_payment = purchase_price * .10
    balance = purchase_price - down_payment
    
    
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Month", "Balance", "Interest", "Principal", "Payment", "Remaining"))
    for i in range (1, 13):
        interest = balance * 0.12 / 12
        monthly_payment = (purchase_price * 0.05) - interest
        principal = monthly_payment - interest
        remaining_balance = balance - monthly_payment
        
        print("{:<10} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f}".format(i, balance, interest, principal, monthly_payment, remaining_balance))
        balance = remaining_balance
         
print(problem5(float(input("Enter purchase price: ")))) 