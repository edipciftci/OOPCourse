students ={
    2225658: ["Edip", 26, "CE", ["CE382", "CE383", "CS388"], 3.5],
    2225659: ["Elvin", 26, "LW", ["LW401", "LW407", "LW424"], 3.6]
}

def printStudents(students:dict):
    for id, values in students.items():
        print("ID: ", id)
        print("Name: ", values[0])
        print("Age: ", values[1])
        print("Major: ", values[2])
        print("Courses: ", values[3])
        print("GPA: ", values[4])
        print("-"*20)

def addStudent(students:dict, id:int, name:str, age:int, major:str, courses:list, gpa:float):
    print("Adding student: ", name)
    print("-"*20)
    students[id] = [name, age, major, courses, gpa]
    
def deleteStudent(students:dict, id:int):
    print("Deleting student: ", students[id][0])
    print("-"*20)
    students.pop(id)

printStudents(students)

newStudent = [2225660, "Can", 26, "IE", ["IE401", "IE412", "IE433"], 3.25]
addStudent(students, newStudent[0], newStudent[1], newStudent[2], newStudent[3], newStudent[4], newStudent[5])

printStudents(students)

deleteStudent(students, 2225658)

printStudents(students)