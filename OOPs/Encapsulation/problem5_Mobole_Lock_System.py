class Mobile:
    def __init__(self):
        self.__pin=None
    def Set_Pin(self,pin):
        self.__pin=pin
    def Unlock(self,pin):
        if self.__pin==pin:
            print("Phone Unlocked")
        else:
            print("Access Denied")
ph1=Mobile()
ph1.Set_Pin("786786")
pin=input("Enter Phone Pin:")
ph1.Unlock(pin)