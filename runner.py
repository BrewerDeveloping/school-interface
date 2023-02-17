from classes.school import School 

# def input_str_to_int(value):
    


school = School('Ridgemont High') 

# print prompt
prompt = """
What would you like to do?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
"""

while(True):
    
    try:
        mode = int(input(prompt))
    
    except ValueError:
        print("Invalid Input, please enter a valid number!")
        continue
    
    if mode == 1:
        student_list = school.get_all_students()
        for student in student_list:
            print(student)
        break
        
    elif mode == 2:
        try:
            id = int(input("Please enter the student's ID. \n>"))
        except ValueError:
            print("Invalid Input, please enter a valid ID number!")
            
        student = school.get_student_by_id(id)
        
        if student : print(student)
        
    elif mode == 3:
        new_student = {}
        new_student['name'] = input('Name: ')
        new_student['age'] = input('Age: ')
        new_student['school_id'] = input('School Id: ')
        new_student['password'] = input('Password: ')
        new_student['role'] = 'Student'
        update_student_list = school.add_student(new_student)
        
        print(update_student_list)
        
    elif mode == 4:
        try:
            id = int(input("Please enter the student's ID. \n>"))
        except ValueError:
            print("Invalid Input, please enter a valid ID number!")
            
            

        update_student_list = school.remove_student_by_id(id)
        
        for student in update_student_list:
            print(student)
        
    elif mode == 5:
        break

