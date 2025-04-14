#დავალება N1

# def collect_names(file_path):
#     counter = 1
#     with open(file_path, "w", encoding="utf-8") as f:
#         while True:
#             first_name = input("Enter your first name: ")
#             if first_name.lower() == "stop":
#                 break
#             last_name = input("Enter your last name: ")
#             f.write(f"{counter}. {first_name} {last_name}\n")
#             counter += 1
#
# if __name__ == "__main__":
#     collect_names("names.txt")
#


# დავალება N2

# def split_by_age(input_file, under_50_file, over_50_file):
#     with open(input_file, "r", encoding="utf-8") as infile, \
#          open(under_50_file, "w", encoding="utf-8") as under_file, \
#          open(over_50_file, "w", encoding="utf-8") as over_file:
#
#         for line in infile:
#             line = line.strip()
#             if not line:
#                 continue
#             try:
#                 parts = [p.strip() for p in line.split(",")]
#                 if len(parts) != 3:
#                     continue
#                 name, age_str, city = parts
#                 age = int(age_str)
#
#                 if age < 50:
#                     under_file.write(f"{line}\n")
#                 elif age > 50:
#                     over_file.write(f"{line}\n")
#             except Exception as e:
#                 print(f"Error: {line} — {e}")
#
# if __name__ == "__main__":
#     split_by_age("persons.txt", "under_50.txt", "over_50.txt")
