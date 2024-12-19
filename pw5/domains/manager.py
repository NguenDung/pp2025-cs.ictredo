from domains.student import Student
from domains.course import Course

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.credits = {}

    def add_student(self, student_id, name, dob):
        self.students.append(Student(student_id, name, dob))

    def add_course(self, course_id, name, credit):
        self.courses.append(Course(course_id, name, credit))
        self.credits[course_id] = credit

    def input_marks(self, course_id, student_scores):
        for student in self.students:
            score = student_scores.get(student.get_id(), 0)
            rounded_score = math.floor(score * 10) / 10
            student.marks[course_id] = rounded_score

    def calculate_gpas(self):
        for student in self.students:
            student.calculate_gpa(self.credits)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)
