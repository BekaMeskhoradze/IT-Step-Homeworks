class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"


class StudentDatabase:
    def __init__(self):
        self.students = [
            Student("Ana", 1, "A"),
            Student("David", 2, "B"),
            Student("Luka", 3, "C"),
            Student("Nino", 4, "A"),
            Student("Saba", 5, "B"),
            Student("Beka", 6, "A"),
            Student("George", 7, "D"),
            Student("Mariam", 8, "A"),
            Student("Eka", 9, "B"),
            Student("Nana", 10, "C"),
        ]
        print("10 students added to the system!\n")

    def add_student(self, student):
        for s in self.students:
            if s.roll_number == student.roll_number:
                print("Error: Roll number already exists.\n")
                return False
        self.students.append(student)
        print("Student added successfully!\n")
        return True

    def view_students(self):
        if not self.students:
            print("No students found.\n")
        else:
            print("Student List:")
            for student in self.students:
                print(student)
        print()

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def update_student_grade(self, roll_number, new_grade):
        student = self.search_student(roll_number)
        if student:
            student.update_grade(new_grade)
            print("Grade updated successfully!\n")
            return True
        print("Student not found.\n")
        return False


class UserInterface:
    def __init__(self):
        self.database = StudentDatabase()

    def get_student_details(self):
        name = input("Enter student name: ")

        while True:
            try:
                roll_number = int(input("Enter roll number: "))
                existing_student = self.database.search_student(roll_number)
                if existing_student:
                    print("Error: Roll number already exists. Please enter a different roll number.\n")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            grade = input("Enter grade (A-F): ").upper().strip()
            if grade in "ABCDEF":
                break
            else:
                print("Grade is required and must be A, B, C, D, or F. Please enter a valid grade.")
        return Student(name, roll_number, grade)

    def run(self):
        while True:
            print("Student Management System")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by Roll Number")
            print("4. Update Student Grade")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                student = self.get_student_details()
                self.database.add_student(student)
            elif choice == "2":
                self.database.view_students()
            elif choice == "3":
                try:
                    roll_number = int(input("Enter roll number to search: "))
                    student = self.database.search_student(roll_number)
                    print(student if student else "Student not found.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
            elif choice == "4":
                try:
                    roll_number = int(input("Enter roll number to update grade: "))
                    new_grade = input("Enter new grade (A-F): ").upper()
                    while new_grade not in "ABCDEF":
                        print("Invalid grade. Enter a valid grade (A-F).")
                        new_grade = input("Enter grade (A-F): ").upper()
                    self.database.update_student_grade(roll_number, new_grade)
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
