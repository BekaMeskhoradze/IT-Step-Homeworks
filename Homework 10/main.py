# დავალება 1

# lst = [(1, 3), (4, 2), (2, 5)]
# sorted_lst = sorted(lst, key=lambda x: x[1])
# print(sorted_lst)

# დავალება 2

# def divide_numbers():
#     try:
#         num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
        
#         result = num1 / num2
#         print(f"გაყოფის შედეგი: {result}")
    
#     except ValueError:
#         print("შეცდომა: გთხოვთ შეიყვანოთ მხოლოდ მთელი რიცხვები!")
    
#     except ZeroDivisionError:
#         print("შეცდომა: ნულზე გაყოფა არ შეიძლება!")


#დავალება 3

# from functools import reduce

# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# filter() - პროდუქტები, რომელთა ფასი ნაკლებია 100-ზე
# filtered_products = list(filter(lambda x: x['price'] < 100, products))
# print("Filtered products (price < 100):")
# print(filtered_products)


# mapped_products = list(map(lambda x: (x['name'], x['price']), products))
# print("\nMapped products (name and price):")
# print(mapped_products)


# sorted_products = sorted(products, key=lambda x: x['price'])
# print("\nSorted products by price:")
# print(sorted_products)


# total_price = reduce(lambda acc, x: acc + x['price'], products, 0)
# print("\nTotal price of all products:")
# print(total_price)
