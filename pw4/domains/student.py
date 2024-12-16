import math

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.marks = {}
        self.gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_gpa(self):
        return self.gpa

    def calculate_gpa(self, credits):
        total_weighted_sum = sum(self.marks[course_id] * credits[course_id] for course_id in self.marks)
        total_credits = sum(credits[course_id] for course_id in self.marks)
        if total_credits > 0:
            self.gpa = round(total_weighted_sum / total_credits, 2)
