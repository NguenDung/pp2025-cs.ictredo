class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id  # Encapsulated attributes
        self.__name = name
        self.__dob = dob

    # Getter methods for encapsulation
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        course = next((c for c in self.courses if c.get_id() == course_id), None)
        if not course:
            print("Course not found!")
            return

        if course_id not in self.marks:
            self.marks[course_id] = {}

        for student in self.students:
            mark = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
            self.marks[course_id][student.get_id()] = mark

    # Display functions
    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"ID: {course.get_id()}, Name: {course.get_name()}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        if course_id not in self.marks:
            print("No marks found for this course!")
            return

        print(f"\nMarks for course {course_id}:")
        for student in self.students:
            mark = self.marks[course_id].get(student.get_id(), "N/A")
            print(f"Student: {student.get_name()} (ID: {student.get_id()}), Mark: {mark}")

    # Menu
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. List students")
            print("2. List courses")
            print("3. Input marks for a course")
            print("4. Show student marks for a course")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.list_students()
            elif choice == 2:
                self.list_courses()
            elif choice == 3:
                self.input_marks()
            elif choice == 4:
                self.show_student_marks()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please try again.")


# Main function
def main():
    manager = MarkManager()
    manager.input_students()
    manager.input_courses()
    manager.menu()


if __name__ == "__main__":
    main()
