from .person import Person
from csv import DictReader


class Staff(Person):
    
    def __init__(self, **kwargs) -> None:
        
        super().__init__(kwargs ['name'], kwargs ['age'], kwargs ['role'], kwargs ['password'])
        self.employee_id = kwargs ['employee_id']
      
      
    @classmethod
    def load_staff_from_csv(cls):
        
        staff_list =[]
        with open('./data/staff.csv') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_staff = cls(**row)
                staff_list.append(new_staff)
                # print(row)
        return staff_list