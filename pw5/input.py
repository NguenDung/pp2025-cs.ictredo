def save_students_to_file(students):
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student.id},{student.name},{student.dob}\n")


def save_courses_to_file(courses):
    with open("courses.txt", "w") as file:
        for course in courses:
            file.write(f"{course.id},{course.name},{course.credits}\n")


def save_marks_to_file(marks):
    with open("marks.txt", "w") as file:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                file.write(f"{course_id},{student_id},{mark}\n")


def load_students_from_file():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                id, name, dob = line.strip().split(",")
                students.append(Student(id, name, dob))
    except FileNotFoundError:
        pass
    return students


def load_courses_from_file():
    courses = []
    try:
        with open("courses.txt", "r") as file:
            for line in file:
                id, name, credits = line.strip().split(",")
                courses.append(Course(id, name, int(credits)))
    except FileNotFoundError:
        pass
    return courses


def load_marks_from_file():
    marks = {}
    try:
        with open("marks.txt", "r") as file:
            for line in file:
                course_id, student_id, mark = line.strip().split(",")
                if course_id not in marks:
                    marks[course_id] = {}
                marks[course_id][student_id] = float(mark)
    except FileNotFoundError:
        pass
    return marks


def compress_files():
    import zipfile
    with zipfile.ZipFile("students.dat", "w") as zipf:
        zipf.write("students.txt")
        zipf.write("courses.txt")
        zipf.write("marks.txt")


def decompress_files():
    import zipfile
    import os
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()
