import json
import logging

from src.models.student import Student

# Setup lines: top of the file, outside any function
logger = logging.getLogger(__name__)


class StudentService:

    def __init__(self, data_file):
        self.data_file = data_file

    def get_all_students(self):
        with open(self.data_file) as f:
            data = json.load(f)

        students = []
        for student_dict in data["students"]:
            students.append(Student.from_dict(student_dict))
        return students

    def add_student(self, student):
        with open(self.data_file) as f:
            data = json.load(f)

        for existing in data["students"]:
            if existing["id"] == student.student_id:
                logger.warning("Add failed: ID %s already exists", student.student_id)
                return False

        data["students"].append(student.to_dict())

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

        logger.info("Added student %s (ID %s)", student.name, student.student_id)
        return True

    def delete_student(self, student_id):
        with open(self.data_file) as f:
            data = json.load(f)

        for student in data["students"]:
            if student["id"] == student_id:
                data["students"].remove(student)
                with open(self.data_file, "w") as f:
                    json.dump(data, f, indent=4)
                logger.info("Deleted student ID %s", student_id)
                return True

        logger.warning("Delete failed: no student with ID %s", student_id)
        return False

    def update_student(self, student_id, name=None, course=None,
                       campus=None, scholar=None):
        with open(self.data_file) as f:
            data = json.load(f)

        for student in data["students"]:
            if student["id"] == student_id:
                if name is not None:
                    student["name"] = name
                if course is not None:
                    student["course"] = course
                if campus is not None:
                    student["campus"] = campus
                if scholar is not None:
                    student["scholar"] = scholar

                with open(self.data_file, "w") as f:
                    json.dump(data, f, indent=4)
                logger.info("Updated student ID %s", student_id)
                return True

        logger.warning("Update failed: no student with ID %s", student_id)
        return False