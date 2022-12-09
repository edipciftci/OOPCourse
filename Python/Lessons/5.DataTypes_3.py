# Dictionaries

student1 = {'name': 'John', 
            'age': 25, 
            'courses': ['Math', 'CompSci']}

student2 = {'name': 'Jane', 
            'age': 26, 
            'courses': ['Math', 'Physics']}
            
student3 = {'name': 'Mary', 
            'age': 27, 
            'courses': ['Math', 'CompSci', 'Physics']}
            
student4 = {'name': 'Mark', 
            'age': 28, 
            'courses': ['Math', 'CompSci', 'Chemistry']}

students = [student1, student2, student3, student4]

for student in students:
    print(student['name'])
    print(student['age'])
    print(student['courses'])
    print("_" * 20)