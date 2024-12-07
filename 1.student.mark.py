

def input_students():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob})
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})
    return courses

def input_marks(students, courses):
    marks = {}
    course_id = input("Enter the course ID to input marks: ")
    course = next((course for course in courses if course["id"] == course_id), None)
    if not course:
        print("Course not found!")
        return marks

    marks[course_id] = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark
    return marks

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_student_marks(students, courses, marks):
    course_id = input("Enter the course ID to view marks: ")
    if course_id not in marks:
        print("No marks found for this course!")
        return

    print(f"\nMarks for course {course_id}:")
    for student in students:
        student_id = student['id']
        mark = marks[course_id].get(student_id, "N/A")
        print(f"Student: {student['name']} (ID: {student_id}), Mark: {mark}")



students = input_students()
courses = input_courses()
marks = {}

while True:
    print("\nMenu:")
    print("1. List students")
    print("2. List courses")
    print("3. Input marks for a course")
    print("4. Show student marks for a course")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        list_students(students)
    elif choice == 2:
        list_courses(courses)
    elif choice == 3:
        new_marks = input_marks(students, courses)
        marks.update(new_marks)
    elif choice == 4:
        show_student_marks(students, courses, marks)
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
