import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id  # Encapsulated attributes
        self.__name = name
        self.__dob = dob
        self.marks = {}  # Dictionary: {course_id: score}
        self.gpa = 0.0   # GPA attribute

    # Getter methods for encapsulation
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.gpa

    def calculate_gpa(self, courses, credits):
        total_weighted_sum = 0
        total_credits = 0
        for course_id, score in self.marks.items():
            course_credit = credits.get(course_id, 0)
            total_weighted_sum += score * course_credit
            total_credits += course_credit
        if total_credits > 0:
            self.gpa = round(total_weighted_sum / total_credits, 2)  # 2 decimals


class Course:
    def __init__(self, course_id, name, credit):
        self.__id = course_id
        self.__name = name
        self.__credit = credit

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.credits = {}  # {course_id: credit}

    # Input functions
    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.students.append(Student(student_id, student_name, student_dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            credit = int(input(f"Enter credit for course {course_name}: "))
            self.courses.append(Course(course_id, course_name, credit))
            self.credits[course_id] = credit

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        course = next((c for c in self.courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found!")
            return

        for student in self.students:
            score = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
            rounded_score = math.floor(score * 10) / 10  # Round down to 1 decimal place
            student.marks[course_id] = rounded_score

    # Calculate GPA for all students
    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.courses, self.credits)

    # Sort students by GPA descending
    def sort_students_by_gpa(self):
        self.students = sorted(self.students, key=lambda s: s.get_gpa(), reverse=True)

    # Display functions with curses
    def display_with_curses(self):
        def draw_ui(stdscr):
            stdscr.clear()
            stdscr.addstr(0, 0, "Student GPA Ranking", curses.A_BOLD)
            row = 2
            for student in self.students:
                stdscr.addstr(row, 0, f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")
                row += 1
            stdscr.refresh()
            stdscr.getch()

        self.calculate_gpas()
        self.sort_students_by_gpa()
        curses.wrapper(draw_ui)

    # Menu
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. Display student GPA ranking")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.input_students()
            elif choice == 2:
                self.input_courses()
            elif choice == 3:
                self.input_marks()
            elif choice == 4:
                self.display_with_curses()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please try again.")


# Main function
def main():
    manager = MarkManager()
    manager.menu()


if __name__ == "__main__":
    main()
