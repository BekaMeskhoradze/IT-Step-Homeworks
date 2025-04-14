# from pymongo import MongoClient
#
# client = MongoClient("mongodb://localhost:27017/")
#
# db = client["PP-25"]
#
# students = db["students"]
#
# student_list = [
#     {
#         "name": "Ethan Miller",
#         "age": 20,
#         "grade": "B+",
#         "courses": ["Math", "Computer Science"],
#         "address": {
#         "city": "Austin",
#         "zipcode": "73301"
#         },
#         "attendance": 87
#       },
#       {
#         "name": "Olivia Johnson",
#         "age": 19,
#         "grade": "A",
#         "courses": ["English", "Psychology"],
#         "address": {
#           "city": "San Diego",
#           "zipcode": "92101"
#         },
#         "attendance": 93
#       },
#       {
#         "name": "Mason Anderson",
#         "age": 21,
#         "grade": "B",
#         "courses": ["Economics", "Statistics"],
#         "address": {
#           "city": "Denver",
#           "zipcode": "80202"
#         },
#         "attendance": 90
#       },
#       {
#         "name": "Ava Martinez",
#         "age": 22,
#         "grade": "A-",
#         "courses": ["Biology", "Chemistry"],
#         "address": {
#           "city": "Miami",
#           "zipcode": "33101"
#         },
#         "attendance": 94
#       },
#       {
#         "name": "Logan Thompson",
#         "age": 23,
#         "grade": "C+",
#         "courses": ["History", "Sociology"],
#         "address": {
#           "city": "Phoenix",
#           "zipcode": "85001"
#         },
#         "attendance": 81
#       },
#       {
#         "name": "Sophia White",
#         "age": 18,
#         "grade": "B-",
#         "courses": ["Art", "Philosophy"],
#         "address": {
#           "city": "Portland",
#           "zipcode": "97201"
#         },
#         "attendance": 86
#       },
#       {
#         "name": "Jackson Taylor",
#         "age": 20,
#         "grade": "A",
#         "courses": ["Engineering", "Physics"],
#         "address": {
#           "city": "Chicago",
#           "zipcode": "60602"
#         },
#         "attendance": 92
#       },
#       {
#         "name": "Isabella Moore",
#         "age": 21,
#         "grade": "B+",
#         "courses": ["Drama", "Music"],
#         "address": {
#           "city": "Los Angeles",
#           "zipcode": "90012"
#         },
#         "attendance": 89
#       },
#       {
#         "name": "Liam Harris",
#         "age": 22,
#         "grade": "C",
#         "courses": ["Geography", "Environmental Studies"],
#         "address": {
#           "city": "New York",
#           "zipcode": "10102"
#         },
#         "attendance": 77
#       }
# ]
#
# students.insert_many(student_list)
#
# # Find all student living in New York
# students_from_ny = students.find({"address.city": "New York"})
#
# for student in students_from_ny:
#     print(f"Name: {student['name']}")
#     print(f"Age: {student['age']}")
#     print(f"City: {student['address']['city']}\n")
#
#
# #Find all students over 18 years old
# students_over_eighteen = students.find({"age": {"$gt": 18}})
#
# for student in students_over_eighteen:
#     print(f"Name: {student['name']}")
#     print(f"Age: {student['age']}\n")
#
#
#
#
# #Find all students who have the course Math
# students_studying_math = students.find({"courses": "Math"})
#
# for student in students_studying_math:
#     print(f"Name: {student['name']}")
#
#
#
# #Count how many students have an A grade.
# a_grade_count = students.count_documents({"grade": "A"})
# if a_grade_count  == 1:
#     print(f"There is {a_grade_count} student who has grade A")
# elif a_grade_count >= 2:
#     print(f"There are {a_grade_count} students who have grade A")
#
# #Count how many students have an A grade.(second way)
# # a_grade_count = 0
# # students_with_grade_a = students.find({"grade": "A"})
# # for student in students_with_grade_a:
# #     a_grade_count += 1
# # if a_grade_count  == 1:
# #     print(f"There is {a_grade_count} student who has grade A")
# # elif a_grade_count >= 2:
# #     print(f"There are {a_grade_count} students who have grade A")
#
#
#
#
#
# #Find all students who live in Los Angeles and have attendance >= 90.
# la_students = students.find({
#     "address.city": "Los Angeles",
#     "attendance": {"$gte": 90}
# })
#
# for student in la_students:
#     print(f"Name: {student['name']}")
#     print(f"Attendance: {student['attendance']}")
#
#
# #Update John Doe's grade to an A grade.
# students.update_one({"name": "John Doe"}, {"$set": {"grader": "A"}})
#
#
# #Add a new field for all students "graduated": false
# students.update_many({}, {"$set": {"graduated": "false"}})
#
#
# #Students with a grade of B, add an "English" course to their courses.
# students.update_many(
#     {"grade": {"$in": ["B", "B-", "B+"]}},
#     {"$addToSet": {"courses": "English"}} #addToSet - avoid adding duplicate(Only if it doesn't exist yet.)
# )
#
#
# #Delete the student whose name is "Alice Smith"
# students.delete_one({"name": "Logan Thompson"})
#
#
# #Delete all students with an attendance rate of less than 60
# students.delete_many({"attendance": {"$lt": 60}})