# student_repo.py
import sqlite3
from student import Student

class StudentRepository:
    """
    Repository Layer Handles all direct database interactions.
    """
    def __init__(self, db_name="school.db"):
        # Connect to the SQLite database 
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the students table if it doesn't already exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade REAL
            )
        ''')
        self.conn.commit()

    def add_student(self, student):
        """Inserts a Student object into the database."""
        self.cursor.execute('''
            INSERT INTO students (student_id, name, age, grade)
            VALUES (?, ?, ?, ?)
        ''', (student.student_id, student.name, student.age, student.grade))
        self.conn.commit()

    def get_students(self):
        """Fetches all students and returns them as a list of Student objects."""
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        
        
        return [Student(row[0], row[1], row[2], row[3]) for row in rows]

    def delete_student(self, student_id):
        """Deletes a student by their ID."""
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()