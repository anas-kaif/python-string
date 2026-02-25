class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def Show_Student(self):
        super().display()
        print("Roll:",self.roll)
s1=Student("Anas","23BTCS036HY")
s1.Show_Student()
