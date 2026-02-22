class Atm:
    def __init__(self):
        self.__balance=0
    def Set_Amout(self,amount):
        self.__balance=amount
    def Get_Amout(self,amount):
        if self.__balance>=amount:
            self.__balance=self.__balance-amount
            print("Take Amount:",amount)

        elif self.__balance<amount:
            return "error You don't have enough balance!"
        
    def Show(self):
        return "Your balance:",self.__balance
    
p1=Atm()
p1.Set_Amout(100000)
print(p1.Show())