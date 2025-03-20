import json


def add_persons_to_json(filename, count):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            persons = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        persons = []

    last_id = persons[-1]["id"] if persons else 0

    for _ in range(count):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        last_id += 1
        persons.append({"id": last_id, "name": name, "age": age})

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(persons, file, indent=4, ensure_ascii=False)

    print("Persons added successfully!")
add_persons_to_json("persons.json", int(input("How many persons do you want to add? ")))