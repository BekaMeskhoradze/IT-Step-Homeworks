from faker import Faker
import random
import json

faker = Faker()

students = [
    {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "age": random.randint(18,70),
        "is_active": random.choice([True, False])
    }
    for _ in range(100)
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    students_data = json.load(file)

active_students = [student for student in students_data if student["is_active"]]

with open("active_students.json", "w") as file:
    json.dump(active_students, file, indent=4)

print("Files created successfully!")