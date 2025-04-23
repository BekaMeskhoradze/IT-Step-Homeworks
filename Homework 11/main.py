# დავალება N1
def add_persons():
    filename = "C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 11\\new_persons.txt"
    count = 1
    try:
        with open(filename, 'x') as file:
            while True:
                first_name = input("Enter the first name: ")
                if first_name.lower() == "stop":
                    break
                last_name = input("Enter the last name: ")
                line = f"{count}. {first_name} {last_name}\n"
                file.write(line)
                count +=1
    except FileExistsError:
        with open(filename, 'w') as file:
            while True:
                first_name = input("Enter the first name: ")
                if first_name.lower() == "stop":
                    break
                last_name = input("Enter the last name: ")
                line = f"{count}. {first_name} {last_name}\n"
                file.write(line)
                count +=1
add_persons()

# დავალება N2
# filename = "C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 11\\persons.txt"
# under_50_txt = "C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 11\\under_50.txt"
# over_50_txt = "C:\\Users\\beqam\\OneDrive\\Desktop\\IT Step Homeworks\\Homework 11\\over_50.txt"
#
# def split_by_age(input_file, under_50_file, over_50_file):
#     with open(filename, 'r') as infile, \
#          open(under_50_txt, 'w') as under50, \
#          open(over_50_txt, 'w') as over50:
#
#         for line in infile:
#             parts = line.strip().split(', ')
#             if len(parts) != 3:
#                 continue
#
#             try:
#                 age = int(parts[1])
#                 if age < 50:
#                     under50.write(line)
#                 elif age > 50:
#                     over50.write(line)
#             except ValueError:
#                 continue
#
# if __name__ == "__main__":
#     split_by_age(filename, under_50_txt, over_50_txt)
#     print("Files are created")
