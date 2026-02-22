class BankAccount:
    def __init__(self):
        self.__balance=0

    def Set_Amount(self,amount):
        self.__balance=amount

    def Get_Amount(self):
        return self.__balance
a1=BankAccount()
print(a1.Get_Amount())
a1.Set_Amount(10000)
print(a1.Get_Amount())  
print(a1.__balance)  #__balance variable directly not accesseble for object