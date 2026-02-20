class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def bonus(self):
        result=self.salary*1.1
        return result
    
    def Show(self):
        print("Salary:",self.bonus())

em1=Employee("Md Kaif",55000)
#em1.bonus()
em1.Show()