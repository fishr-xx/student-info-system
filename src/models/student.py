class Student:
    def __init__(self, name, student_id, course, campus, scholar):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.campus = campus
        self.scholar = scholar

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.student_id,
            "course": self.course,
            "campus": self.campus,
            "scholar": self.scholar
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            student_id=data["id"],
            course=data["course"],
            campus=data["campus"],
            scholar=data["scholar"]
        )