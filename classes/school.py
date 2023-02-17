from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.staff = Staff.load_staff_from_csv()
        self.students = Student.load_student_from_csv()

    