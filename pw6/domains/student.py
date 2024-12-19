class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def to_dict(self):
        return {"id": self.id, "name": self.name, "dob": self.dob}

    @staticmethod
    def from_dict(data):
        return Student(data["id"], data["name"], data["dob"])
