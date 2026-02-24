class Employee:
    #name=None
    def __init__(self,name):
        self.name=name

    def Show(self):
        print("Employee name:",self.name)
class Manager(Employee):
    def __init__(self,name,salary):
        self.salary=salary
        super().__init__(name)
    def Show(self):
        super().Show()
        print("Salary:",self.salary)

    

M1=Manager("Anas",55000)
M1.Show()

