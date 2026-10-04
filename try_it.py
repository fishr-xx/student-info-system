from src.services.student_service import StudentService

service = StudentService("data/students.json")

for student in service.get_all_students():
    print()
    print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}, Campus:{student.campus}, Scholarship: {student.scholar}")
    print("-----------------------------")

print(service.update_student(266, campus="Urdaneta"))   
print(service.update_student(555, campus="Urdaneta"))
