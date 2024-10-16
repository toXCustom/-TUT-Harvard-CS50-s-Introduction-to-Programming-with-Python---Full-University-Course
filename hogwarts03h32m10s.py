students = {
    "Hermonie": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}

#print(students["Hermonie"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

for student in students:
    print(student, students[student], sep=", ")