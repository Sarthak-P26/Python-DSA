class Player():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def printing(self):
        print(f"The student we have is {self.type} and his name is {self.name}")

class Student(Player):
    def __init__(self, name, type, age):
        super().__init__(name, type)
        self.age = age

    def printing(self):
        print(f"The student age is {self.age} his name is {self.name} he is a {self.type}")
    

student1 = Player("sujeet","Gay")
student2 = Student("Sarthak", "Man", 21)
student2.printing()

