
def read_csv(filename):
    fp      =   open(filename, "r", encoding="utf-8")
    data    =   fp.read()
    fp.close()

    elements=[]

    rows = data.split('\n')

    for row in rows:
        fields = row.split(",")

        name    = fields[0].strip()
        school  = fields[1].strip()
        email   = fields[2].strip()

        element = {"이름" : name, "학교" : school, "메일" : email }
        elements.append(element)

    return elements

filename = "./data/student.csv"
students = read_csv(filename)

print(students)

for student in students:
    print(student)

print('*'*50)
print(students[0]['이름'])