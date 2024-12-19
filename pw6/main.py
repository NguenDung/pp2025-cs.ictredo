from input import (
    save_students_to_file, save_courses_to_file, save_marks_to_file,
    load_students_from_file, load_courses_from_file, load_marks_from_file,
    compress_files, decompress_files,
)

if __name__ == "__main__":
    # Load persistent data if exists
    decompress_files()
    students = load_students_from_file()
    courses = load_courses_from_file()
    marks = load_marks_from_file()

    # Save and compress data before exiting
    save_students_to_file(students)
    save_courses_to_file(courses)
    save_marks_to_file(marks)
    compress_files()
