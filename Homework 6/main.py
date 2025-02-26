# დავალება N1
# square_dict = {i:i**2 for i in range(1, 11)}
# print(square_dict)

#დავალება N2
# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]
#
# for product in products:
#     for name in product:
#         print(name)
#
# total_value = 0
# for product in products:
#     for name, details in product.items():
#         total_value += details["price"] * details["quantity"]
# print("ჯამური ღირებულება:", total_value)


#დავალება N3
# fruit_counts = {}
#
# while True:
#     fruit = input("Enter your favorite fruit: ").strip()
#     if fruit.lower() == 'stop':
#         break
#     if fruit in fruit_counts:
#         fruit_counts[fruit] += 1
#     else:
#         fruit_counts[fruit] = 1
#
# print(fruit_counts)