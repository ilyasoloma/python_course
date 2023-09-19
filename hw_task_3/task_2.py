class student:
    def __init__(self):
        self.knowledge = []
    def take(self, line_knowledge):
        self.knowledge.append(line_knowledge)

class Teacher:
    def __init__(self):
        self.count_trained = 0
    def teach(self, name_material, count_student = None):
        for i in range(count_student):
            students[i].take(name_material)
            self.count_trained += 1

class edu_materials:
    def __init__(self, *args):
        self.material = []
        for line in args:
            self.material.append(line)

DB_material = edu_materials("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")
teacher = Teacher()
students = [student() for i in range(0, 4)]
for i in range(0, 4):
    if i+1 < 5:
        teacher.teach(DB_material.material[i], i+1)
    else:
        teacher.teach(DB_material.material[i], i)
print(teacher.count_trained)


