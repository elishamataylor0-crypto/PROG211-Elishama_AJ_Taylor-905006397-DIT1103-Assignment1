"""
Project: Student Learning Portal
Course: PROG211 - Object-Oriented Programming 1

This program stores and displays fictional student records using OOP.
It demonstrates classes, objects, a dictionary, instance methods,
a class method, and interaction between objects.
"""


class Student:
    """Represents a student in the learning portal."""

    school_name = "Student Learning Portal"

    def __init__(self, student_id, name, course, level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.level = level

    def display_info(self):
        """Display this student's information."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Level: {self.level}")

    def update_course(self, new_course):
        """Update this student's course."""
        self.course = new_course
        print(f"{self.name}'s course has been updated.")

    @classmethod
    def change_school_name(cls, new_name):
        """Update the class-level portal name."""
        cls.school_name = new_name


class LearningPortal:
    """Manage student records in a dictionary."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        """Add a Student object, preventing duplicate IDs."""
        if student.student_id in self.students:
            print("Error: This student ID already exists.")
            return

        self.students[student.student_id] = student
        print(f"{student.name} has been added successfully.")

    def display_students(self):
        """Display all student records."""
        if not self.students:
            print("No student records available.")
            return

        print("\\n===== ALL STUDENT RECORDS =====")
        for student in self.students.values():
            print("-" * 30)
            student.display_info()

    def search_student(self, student_id):
        """Search for a student by ID."""
        student = self.students.get(student_id)

        if student is not None:
            print("\\n===== STUDENT FOUND =====")
            student.display_info()
        else:
            print("Student not found.")

    def remove_student(self, student_id):
        """Remove a student by ID."""
        student = self.students.pop(student_id, None)

        if student is not None:
            print(f"{student.name} has been removed.")
        else:
            print("Student not found.")


def main():
    """Create example records and demonstrate the portal features."""
    portal = LearningPortal()

    student1 = Student("ST001", "Student One", "Information Technology", 1)
    student2 = Student("ST002", "Student Two", "Software Engineering", 1)
    student3 = Student("ST003", "Student Three", "Computer Science", 2)

    portal.add_student(student1)
    portal.add_student(student2)
    portal.add_student(student3)

    Student.change_school_name("Open Student Learning Portal")
    print(f"\\nPortal Name: {Student.school_name}")

    portal.display_students()

    print("\\n===== SEARCH STUDENT =====")
    portal.search_student("ST002")

    print("\\n===== UPDATE STUDENT COURSE =====")
    student1.update_course("Artificial Intelligence")
    student1.display_info()

    print("\\n===== REMOVE STUDENT =====")
    portal.remove_student("ST003")

    portal.display_students()


if __name__ == "__main__":
    main()
