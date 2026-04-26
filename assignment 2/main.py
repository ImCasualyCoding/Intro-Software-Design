# main.py
from student_repo import StudentRepository
from student_service import StudentService

def main():
  
    # Setup our layers 
    repo = StudentRepository()
    service = StudentService(repo)

    while True:
        # Display the main menu
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View Students")
        print("3. Delete student")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # Handle adding a student
            try:
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                grade = float(input("Enter Student Grade: "))
                
                
                service.add_student(student_id, name, age, grade)
                print(f"Success: Student {name} added successfully.")
            except ValueError as e:
                # Catch either type conversion errors 
                # or business logic errors 
                print(f"Error: {e}")
            except Exception as e:
                 print(f"Database Error: {e} (ID might already exist)")

        elif choice == '2':
            # Handle viewing students
            students = service.get_students()
            if not students:
                print("No students found in the database.")
            else:
                print("\n--- Student List ---")
                for student in students:
                    print(student) # This calls the __str__ method we defined in student.py

        elif choice == '3':
            # Handle deleting a student
            student_id = input("Enter the ID of the student to delete: ")
            service.delete_student(student_id)
            print(f"Student {student_id} has been deleted (if they existed).")

        elif choice == '4':
            # Exit the loop and end the program
            print("Exiting the Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()