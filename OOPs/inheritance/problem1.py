class Person:
    name=None
    def display(self):
        print("Person name:",self.name)
class Student(Person):
    roll_no=None
    def Show_Student(self):
        print("Student name:",self.name)
        print("Student Roll No.:",self.roll_no)
s1=Student()
s1.name="Anas"
s1.display()
s1.roll_no="23btcs036hy"
s1.Show_Student()
