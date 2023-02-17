from .person import Person
import csv


class Staff(Person):
    
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
        
    def load_staff_from_csv():
        
        
        with open('./data/staff.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)