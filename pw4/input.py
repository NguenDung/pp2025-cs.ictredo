def input_students(manager):
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB (DD/MM/YYYY): ")
        manager.add_student(student_id, name, dob)

def input_courses(manager):
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input(f"Enter credit for {name}: "))
        manager.add_course(course_id, name, credit)

def input_marks(manager):
    course_id = input("Enter course ID: ")
    student_scores = {}
    for student in manager.students:
        score = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
        student_scores[student.get_id()] = score
    manager.input_marks(course_id, student_scores)
