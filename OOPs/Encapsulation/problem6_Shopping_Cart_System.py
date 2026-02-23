class Cart:
    def __init__(self):
        self.__cart={}
    def Add_item(self,name,price):
        self.__cart.update({name:price})

    def Show_items(self):
        for k,v in self.__cart.items():
            print(k,":",v)
    def Remove_items(self,name):
        self.__cart.pop(name)
    def Show_total(self):
        total=0
        for values in self.__cart.values():
            total+=values
        return total
sp1=Cart()

print("Welcome to Cart System!\n")
print("(1)Add items      (2)Remove item\n(3)Show items      (4)Show total\n(5)Exit")
choice=0
while choice != 5:
    choice=int(input("Enter your option:"))

    if choice==1:
        name=input("Enter item name:")
        price=int(input("Enter item price:"))
        sp1.Add_item(name,price)

    elif choice==2:
        name=input("Enter item to remove:")
        sp1.Remove_items(name)

    elif choice==3:
        sp1.Show_items()

    elif choice==4:
        print("Total:",sp1.Show_total())

    elif choice==5:
        print("Thank you!")

    else:
        print("Invalid option")