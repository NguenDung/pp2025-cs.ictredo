class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

    def to_dict(self):
        return {"id": self.id, "name": self.name, "credits": self.credits}

    @staticmethod
    def from_dict(data):
        return Course(data["id"], data["name"], data["credits"])
