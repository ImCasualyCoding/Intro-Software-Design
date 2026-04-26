# student_service.py
from student import Student

class StudentService:
    """
    Service Layer: Contains the core business logic and validations.
    Depends on the repository layer through Dependency Injection.
    """
    def __init__(self, repository):
        # Dependency Inversion:  pass the repository into the service.
        self.repository = repository

    def add_student(self, student_id, name, age, grade):
        """Validates data and adds a new student via the repository."""
        # Business Rule 1 Age must be greater than 15
        if age <= 15:
            raise ValueError("Student age must be greater than 15.")
        
        # Business Rule 2 Grade must be greater than 70
        if grade <= 70:
            raise ValueError("Student grade must be greater than 70.")

        # If validations pass, create the model and send to the repository
        student = Student(student_id, name, age, grade)
        self.repository.add_student(student)

    def get_students(self):
        """Fetches all students by delegating to the repository."""
        return self.repository.get_students()

    def delete_student(self, student_id):
        """Deletes a student by delegating to the repository."""
        self.repository.delete_student(student_id)