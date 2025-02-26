# დავალება N1

#user_input = int(input("Enter the number: "))

#for i in range(5, 0, -1):
#    print(f"{user_input} * {i} = ",user_input * i)

# დავალება N2

#for i in range(1, 11):
#    for j in range(1, 11):
#        print(f"{i} * {j} =", i * j)


# დავალება N3

total_cost = 50
total_paid = 0

while total_paid < total_cost:
    bill = int(input("Pay(5$, 10$ or 20$): "))

    if bill == 5 or bill == 10 or bill == 20:
        total_paid += bill
        remaining = total_cost - total_paid

        if remaining > 0:
            print(f"Remaining amount: {remaining}$")
        else:
            change = total_paid - total_cost
            if change > 0:
                print(f"Already paid. Your change is {change}$!")
            else:
                print("Already paid. Thank you!")
            break
    else:
        print("Enter valid amount (5$, 10$ or 20$)")
