from classes.school import School 

school = School('Ridgemont High') 

# print prompt


print(school.name)

for s in school.staff:
    print(s.name)
    
for s in school.students:
    print(s.name)