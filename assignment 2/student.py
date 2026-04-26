# student.py

class Student:

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        # A helper method to print the student object nicely
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade}"