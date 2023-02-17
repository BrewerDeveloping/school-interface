from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.staff = Staff.load_staff_from_csv()
        self.students = Student.load_student_from_csv()

    def get_all_students(self):
        return self.students
    
    def get_student_by_id(self, id):
        
        for student in self.students:

            
            if student.school_id == id:
                return student
            
        print("She doesnt even go here")
        return
    
    def add_student(self, new_student):
        
        self.students.append(Student(**new_student))
        return self.students
    
    def remove_student_by_id(self, id):
        
        for student in self.students:
            if student.school_id == id:
                self.students.remove(student)
                return self.students
        print("Couldn't find student")
        return