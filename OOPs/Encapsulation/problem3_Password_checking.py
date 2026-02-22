class User:
    def __init__(self):
        self.__password=None
    def Set_Paswd(self,paswd):
        self.__password=paswd
    def Check_Paswd(self,paswd):
        return self.__password==paswd
    
usr1=User()
usr1.Set_Paswd("843119Mm@")
usr1.password="anaskaif"
paswd=input("Enter Your Password:")
print(usr1.Check_Paswd(paswd))