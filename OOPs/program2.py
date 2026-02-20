class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def result(self):
        result=self.length*self.breath
        return result

length=int(input("Enter Length of Rectangle:"))
breath=int(input("Enter breath of Rectangle:"))
s1=Rectangle(length,breath)
print("Area of Rectangle is:",s1.result())