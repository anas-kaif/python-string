class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)

s1=Student("Anas",22)
s1.name="kaif"
s1.age=20
s1.show()