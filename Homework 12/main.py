import csv

def collect_user_data(num_users):
    with open('users.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['ID', 'first_name', 'last_name', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(1, num_users + 1):
            print(f"\nUser #{i}")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            while True:
                try:
                    age = int(input("Enter age: "))
                    break
                except ValueError:
                    print("Please enter a valid number for age!")

            writer.writerow({
                'ID': i,
                'first_name': first_name,
                'last_name': last_name,
                'age': age
            })
    print("\nData has been successfully written to the 'users.csv' file.")
