#დავალება N1
# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# while True:
#     first_name = input("Enter first name (or type 'stop' to end): ").strip()
#     if first_name.lower() == 'stop':
#         break
#
#     last_name = input("Enter last name (or type 'stop' to end): ").strip()
#     if last_name.lower() == 'stop':
#         break
#
#     found = False
#     for person in persons:
#         if person[0].lower() == first_name.lower() and person[1].lower() == last_name.lower():
#             print(f"Age: {person[2]}")
#             found = True
#             break
#
#     if not found:
#         print("Person not found.")

# დავალება N2
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

set1 = set(word1)
set2 = set(word2)

common_characters = set1 & set2
unique_characters = set1 ^ set2
union_characters = set1 | set2

print("Common characters:", common_characters)
print("Unique characters:", unique_characters)
print("Union characters:", union_characters)