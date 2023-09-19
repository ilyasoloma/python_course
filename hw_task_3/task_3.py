from random import randint
class Human:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender


class Student(Human):
    def __init__(self, full_name, age, gender):
        self.knowledge = []
        super().__init__(full_name, age, gender)

    def take(self, line_knowledge):
        self.knowledge.append(line_knowledge)

    def __len__(self):
        return len(self.knowledge)


    def forget_knowledge(self):
        start_index = randint(0, len(self)-1)
        end_index = randint(start_index, len(self)-1)
        for i in range(start_index, end_index):
            self.knowledge.pop(i)

class Teacher(Human):
    def __init__(self, full_name, age, gender):
        self.count_trained = 0
        super().__init__(full_name, age, gender)

    def teach(self, name_material, count_student=None):
        for i in range(count_student):
            students[i].take(name_material)
            self.count_trained += 1


class Edu_materials:
    def __init__(self, *args):
        self.material = []
        for line in args:
            self.material.append(line)

    def __len__(self):
        return len(self.material)


DB_material = Edu_materials("Python", "Version Control Systems", "Relational Databases", "NoSQL databases",
                            "Message Brokers")
teacher = Teacher("SS SDFS SF", 30, "Male")
students = [Student(f"ded{i}", 19+i, "Male") for i in range(0, 4)]
for i in range(0, 4):
    if i + 1 < 5:
        teacher.teach(DB_material.material[i], i + 1)
    else:
        teacher.teach(DB_material.material[i], i)

students[2].forget_knowledge()
for student in students:
    print(len(student))

