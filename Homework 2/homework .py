# დავალება N1

# weight = float(input("Enter your weight(kg): "))
# height = float(input("Enter your height(m): "))
# bmi = weight / height ** 2
#
# if 0 < bmi < 19:
#     print(f"Your BMI is {bmi}. You are underweight")
# elif 19 < bmi < 25:
#     print(f"Your BMI is {bmi}. You are normalweight")
# elif bmi > 25:
#     print(f"Your BMI is {bmi}. You are overweight")
# else:
#     print("You entered invalid weight or height")

#დავალება N2

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# operation = str(input("Enter the operator: "))
# num3 = 0
#
# match operation:
#     case "+":
#        num3 += num1 + num2
#        print(num3)
#     case "-":
#        num3 += num1 - num2
#        print(num3)
#
#     case "*":
#        num3 += num1 * num2
#        print(num3)
#
#     case "/":
#         num3 += num1 / num2
#         print(num3)
#     case _:
#         print("Invalid operation")

# დავალება N3
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# if num1 != num2 and num1 != num3 and num2 != num3:
#     if num2 < num1 > num3:
#         print(num1)
#     elif num1 < num2 > num3:
#         print(num2)
#     else:
#         print(num3)
# else:
#     print("You entered same numbers, please enter the different numbers")