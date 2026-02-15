class Student:
    name="Anas"
    age=21
    def __init__(self):
        print("hello")
    def __init__(self,name):
        self.name=name

s1=Student()
print(s1.name)