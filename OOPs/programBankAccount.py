class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,Amount):
        self.balance=self.balance+Amount

    def withdrawl(self,Amount):
        self.balance=self.balance-Amount

    def show_balance(self):
        print("Your Balance:",self.balance)

Act1=BankAccount(5500)
Act1.show_balance()
Act1.deposit(1200)
Act1.show_balance()
Act1.withdrawl(700)
Act1.show_balance()