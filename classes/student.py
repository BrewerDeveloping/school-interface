from classes.person import Person
from csv import DictReader

class Student(Person):
    
    def __init__(self, **kwargs) -> None:
        super().__init__(kwargs ['name'], kwargs ['age'], kwargs ['role'], kwargs ['password'])
        self.school_id = int(kwargs["school_id"])
        
    @classmethod    
    def load_student_from_csv(cls):
        
        student_list =[]
        with open('./data/students.csv') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_student = cls(**row)
                student_list.append(new_student)
                # print(row)
        return student_list
    
    def __str__(self) -> str:
        return f"Name: {self.name} -- Age: {self.age} -- ID: {self.school_id}"