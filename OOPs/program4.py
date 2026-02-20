class Calculator:
    def __init__(self,operant1,operant2):
        self.operant1=operant1
        self.operant2=operant2

    def Add(self):
        add=self.operant1+self.operant2
        return add
    def Subtract(self):
        return self.operant1-self.operant2
    def Multiply(self):
        return self.operant1*self.operant2
    
operant1=int(input("Enter First Number:"))
operant2=int(input("Enter Second Number:"))
operand=input("Enter Operand:")
if operand=='+':
    op=Calculator(operant1,operant2)
    print("Result:",op.Add())