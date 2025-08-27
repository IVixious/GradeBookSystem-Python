# Question 4:
# Create a simple grade book system
# Feature
# -Add student
# -Remove student
# -Update Grade
# -Display student info
# -Get top students


# Dictionary to store student data
students = {}


# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    grade = float(input(f"Enter {name}'s grade: "))
    students[name] = grade
    print(f"{name} added to the gradebook with grade {grade}.")


# Function to remove a student
def remove_student():
    name = input("Enter student's name to remove: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed from the gradebook.")
    else:
        print(f"Student {name} not found in the gradebook.")


# Function to update a student's grade
def update_grade():
    name = input("Enter student's name to update grade: ")
    if name in students:
        new_grade = float(input(f"Enter new grade for {name}: "))
        students[name] = new_grade
        print(f"{name}'s grade has been updated to {new_grade}.")
    else:
        print(f"Student {name} not found in the gradebook.")


# Function to display all students' info
def display_students():
    if students:
        print("\nStudent Info:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No students in the gradebook.")


# Function to get the top student(s)
def get_top_students():
    if students:
        top_student = max(students, key=students.get)  # Get the student with the highest grade
        print(f"Top student: {top_student} with grade {students[top_student]}")
    else:
        print("No students in the gradebook.")



# Main program loop
def main():
    while True:
        print("\nGradebook System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Grade")
        print("4. Display Student Info")
        print("5. Get Top Student(s)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_grade()
        elif choice == "4":
            display_students()
        elif choice == "5":
            get_top_students()
        elif choice == "6":
            print("Exiting gradebook system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
