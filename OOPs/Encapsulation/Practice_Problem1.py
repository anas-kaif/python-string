class Student:
    def __init__(self):
        self.__name=None

    def Set_name(self,name):
        self.__name=name

    def Get_name(self):
        return self.__name

s1=Student()
print(s1.Get_name())
s1.Set_name("Anas")
print(s1.Get_name())
s1.__name="kaif"   #new private variable
print(s1.__name)   #output:-kaif
print(s1.Get_name())  #output:-Anas         because class variable __name can't access directly