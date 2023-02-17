from classes.person import Person
import csv

class Student(Person):
    
    def __init__(self, name, age, role, student_id, password):
        super().__init__(name, age, role, password)
        self.student_id = student_id
        
        
    # def load_student_from_csv():
        
    #     with open('../data/staff.csv') as csv_file:
    #         reader = csv.DictReader(csv_file)
    #     pass