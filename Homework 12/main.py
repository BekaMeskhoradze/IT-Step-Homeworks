#დავალება 1
import csv

# def collect_user_data(n):
#     with open('users.csv', 'w', newline='') as csvfile:
#         fieldnames = ['ID', 'first_name', 'last_name', 'age']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for i in range(1, n + 1):
#             print(f"Enter details for user ({i}): ")
#             first_name = input("Enter the name: ").strip()
#             last_name = input("Enter the last name: ").strip()
#
#             while True:
#                 try:
#                     age = int(input("Enter the age: ").strip())
#                     break
#                 except ValueError:
#                     print("Please enter a valid number for age!")
#
#             writer.writerow({
#                 'ID': i,
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'age': age
#             })
#
# collect_user_data(3)

#დავალება 2
#
# input_file_path = 'C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 12\\students.csv'
# failed_output_path = 'C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 12\\failed_students.csv'
# passed_output_path = 'C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 12\\passed_students.csv'
#
#
# with open(input_file_path, 'r') as infile:
#     reader = csv.DictReader(infile)
#     fieldnames = reader.fieldnames
#
#     failed_students = []
#     passed_students = []
#
#     for row in reader:
#         try:
#             grade = int(row['Grade'])
#             if grade <= 50:
#                 failed_students.append(row)
#             else:
#                 passed_students.append(row)
#         except ValueError:
#             continue
#
# with open(failed_output_path, 'w', newline='') as failfile:
#     writer = csv.DictWriter(failfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(failed_students)
#
# with open(passed_output_path, 'w', newline='') as passfile:
#     writer = csv.DictWriter(passfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(passed_students)

