students = [
    {
        "id": 2225658,
        "name": "Edip",
        "age": 26,
        "major": "CE",
        "courses": ["CE382", "CE383", "CS388"],
        "gpa": 3.5
    },
    {
        "id": 2225659,
        "name": "Elvin",
        "age": 26,
        "major": "LW",
        "courses": ["LW401", "LW407", "LW424"],
        "gpa": 3.6
    }
]

def printStudents(students:list):
    for student in students:
        print("ID: ", student["id"])
        print("Name: ", student["name"])
        print("Age: ", student["age"])
        print("Major: ", student["major"])
        print("Courses: ", student["courses"])
        print("GPA: ", student["gpa"])
        print("-"*20)

def addStudent(students:list, id:int, name:str, age:int, major:str, courses:list, gpa:float):
    print("Adding student: ", name)
    print("-"*20)
    students.append({
        "id": id,
        "name": name,
        "age": age,
        "major": major,
        "courses": courses,
        "gpa": gpa
    })

def deleteStudent(students:list, id:int):
    index = findByID(students, id)
    if index == -1:
        print("Student not found!")
        return
    print("Deleting student: ", students[index]["name"])
    print("-"*20)
    students.pop(index)

def findByID(students:list, id:int):
    for i in range(len(students)):
        if students[i]["id"] == id:
            return i
    return -1

printStudents(students)

newStudent = [2225660, "Can", 26, "IE", ["IE401", "IE412", "IE433"], 3.25]

addStudent(students, newStudent[0], newStudent[1], newStudent[2], newStudent[3], newStudent[4], newStudent[5])

printStudents(students)

deleteStudent(students, 2225658)

printStudents(students)